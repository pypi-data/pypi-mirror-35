# -*- coding: utf8 -*-
import hashlib
import logging
import re
import tempfile
import uuid
from os import path, remove
from shutil import copyfile
from traceback import format_exception_only

from six.moves.urllib import parse
from shutil import rmtree, copytree


def export_exception(ex):
    return ('\n'.join(format_exception_only(ex.__class__, ex))).strip()


class GitError(Exception):
    pass


class GitExpando(object):
    pass


def _append_commit_link(remote_template):
    x = parse.urlparse(remote_template)
    if x.hostname is not None:
        remote_template += '/commit/{}' if x.hostname.lower() == 'github.com' else '/commits/{}'
    return remote_template


def ssh_to_https(url):
    if '@' in url:
        return 'https://' + (url.split('@')[1].strip()).replace(':', '/')
    return url


def enforce_https(url):
    if url.startswith('http://'):
        return 'https://' + url[len('http://'):]
    return url


def remove_dot_git(url):
    return url if not url.lower().endswith('.git') else url[:-4]


def remote_to_template(remote_url):
    return remove_dot_git(enforce_https(ssh_to_https(remote_url.lower())))


def get_remote_url():
    try:
        import git
        repo = git.Repo('.', search_parent_directories=True)
        if len(repo.remotes) > 0:
            remote = list(repo.remotes)[0]
            return remote_to_template(remote.url)
    except Exception as gr:
        logging.error("Failed to get remote git repository of current folder. {}".format(str(gr)))
    return None


def remote_url_obj(url):
    if url is None:
        return None

    obj = parse.urlparse(remote_to_template(url))
    if obj.hostname is None or obj.hostname == '':
        return None

    return obj


def get_org_from_remote_url(url):
    url_obj = remote_url_obj(url)
    if url_obj is None:
        return None

    return '/'.join(url_obj.path.split('/')[:-1]).lower()


def validate_diff_urls(src, trg):
    src = remote_to_template(src)
    trg = remote_to_template(trg)
    return src == trg


def validate_remote_urls_org(src, trg):
    src_org = get_org_from_remote_url(src)
    remote_org = get_org_from_remote_url(trg)

    return src_org == remote_org


def __fill_repo(repo, res=GitExpando()):
    res.repo = repo
    res.git_version = repo.git.version()
    res.remote_name = None
    res.remote_url = None
    res.has_head = repo.head.is_valid()
    res._remote_template = None
    if len(repo.remotes) > 0:
        remote = list(repo.remotes)[0]
        res.remote_name = remote.name
        res.remote_url = remote.url
        res._remote_template = _append_commit_link(remote_to_template(remote.url))
    res.branch = repo.active_branch
    res.head_sha = res.repo.head.object.hexsha if res.has_head else None

    res.head_sha_url = res._remote_template.format(res.head_sha) if res._remote_template else res.head_sha
    res.is_clean = repo.git.status(porcelain=True).strip() == ''
    return res


def _export_commit(commit):
    return {'author': commit.author.name,
            'email': commit.author.email,
            'date': commit.authored_datetime.isoformat()}


def import_git():
    try:
        import git
        return git
    except ImportError:
        logging.warning('Failed to import git')
        raise GitError('Failed to import git')


def get_repo(path_=None, repo=None):
    git = import_git()
    try:
        repo = repo or git.Repo(path_, search_parent_directories=True)
        response = __fill_repo(repo)
        response.export_commit = _export_commit
        response.refresh = lambda: __fill_repo(repo, response)
        return response
    except git.exc.GitCommandError as ex:
        logging.warning('Failed to get repo status: {}'.format(export_exception(ex)))
        raise GitError('Failed to get repo status: {}'.format(export_exception(ex)))
    except git.exc.InvalidGitRepositoryError:
        logging.warning('path {} is not tracked'.format(path_))
        raise GitError('path is not tracked')


def try_get_raw_repo(path_='.'):
    try:
        repo = import_git().Repo(path_, search_parent_directories=True)
        return remote_to_template(list(repo.remotes)[0].url)
    except GitError as ex:
        logging.debug('Failed to get local repo path. got: {}'.format(export_exception(ex)))
    except Exception as ex:
        logging.warning('Failed to get local repo path. got: {}'.format(export_exception(ex)))
    return None


class GitRepoSyncer(object):
    @classmethod
    def _sanitize_branch_name(cls, name):
        return re.sub(r'[^a-zA-Z0-9]', "_", name)

    @classmethod
    def try_ex_path(cls, git, repo_path):
        if path.isdir(repo_path):
            try:
                repo = git.Repo(repo_path)
                return repo
            except Exception as ex:
                logging.warning("Failed to init tracking repository repo at {}, got {}".format(repo_path, str(ex)))
                remove(repo_path)
        return None

    @classmethod
    def _validate_tracking_repository_or_clone(cls, repo_path, tracking_origin_url):

        git = import_git()
        repo = cls.try_ex_path(git, repo_path) or git.Repo.clone_from(tracking_origin_url, repo_path)
        for remote in repo.remotes:
            if remote.name == 'origin' and remote.url != tracking_origin_url:
                raise GitError("Tracking repository at {} has remote other than {} tracking_origin_url configured: {}".format(repo_path, tracking_origin_url, remote.url))

        repo.git.reset(hard=True)
        return repo

    @classmethod
    def clone_tracking_repo(cls, tracking_repository_remote_url, fixed_clone_path=None):
        repo_id = 'missinglink_{}'.format(hashlib.sha256(tracking_repository_remote_url.encode('utf-8')).hexdigest())
        temp_path = fixed_clone_path or path.join(tempfile.gettempdir(), repo_id)
        logging.debug("Clone {} to {}".format(tracking_repository_remote_url, temp_path))
        return cls._validate_tracking_repository_or_clone(temp_path, tracking_repository_remote_url)

    @classmethod
    def _checkout(cls, repo, branch=None):
        if branch in repo.branches:
            repo.git.checkout(branch)
        else:
            repo.git.checkout(b=branch)

    @classmethod
    def _get_changed_files(cls, repo):
        changes = repo.git.status(porcelain=True).strip()
        if len(changes) == 0:
            return []

        files = map(lambda x: x.split(' ')[-1].strip(), repo.git.status(porcelain=1).strip().split('\n'))

        return list(files)

    @classmethod
    def _copy_path(cls, src_file, tracked_file):
        if not path.exists(src_file):
            return False

        if path.isdir(src_file):
            if path.exists(tracked_file):
                rmtree(tracked_file, ignore_errors=True)

            copytree(src_file, tracked_file)
            return True

        copyfile(src_file, tracked_file)
        return True

    @classmethod
    def _remove_path(cls, tracked_file):
        if not path.exists(tracked_file):  # the file is deleted - delete it
            return

        if path.isdir(tracked_file):
            rmtree(tracked_file)
            return

        remove(tracked_file)
        return

    @classmethod
    def _sync_uncommitted_changes(cls, src, tracking):
        changed_files = cls._get_changed_files(src)
        for changed_file in changed_files:
            src_file = path.join(src.working_dir, changed_file)
            tracked_file = path.join(tracking.working_dir, changed_file)
            logging.debug('_sync_uncommitted_changes %s -> %s', src_file, tracked_file)

            if not cls._copy_path(src_file, tracked_file):  # the file is present, copy it...
                cls._remove_path(tracked_file)

        if len(changed_files) > 0:
            tracking.git.add('.')
            tracking.index.commit('ML AI: Synced file(s) from {}.Files: \n{}'.format(src.working_dir, '\n'.join(changed_files)))

    @classmethod
    def _cp_lfs(cls, src, tracking, branch_name):
        import shutil

        src_lfs_path = path.join(src.git_dir, 'lfs')
        tracking_lfs_path = path.join(tracking.git_dir, 'lfs')
        if path.isdir(src_lfs_path):
            logging.info('LFS cache found in source repository. Syncing %s to %s', src_lfs_path, tracking_lfs_path)
            if path.isdir(tracking_lfs_path):
                logging.debug('Remove shadow LFS dir %s', tracking_lfs_path)
                shutil.rmtree(tracking_lfs_path)
            shutil.copytree(src_lfs_path, tracking_lfs_path)

    @classmethod
    def _merge_to_new_branch(cls, src, tracking, branch_name):

        cls._checkout(tracking, 'dev_null')
        tracking.git.fetch('origin')
        cls._cp_lfs(src, tracking, branch_name)
        tracking.git.fetch('src')
        cls._checkout(tracking, branch_name)
        # OK, so why not to sync the current src branch to the target one and then move to the custom branch?
        # Because of branch name collisions
        # lets say Alice and Bob are pullig the src from the same head `HEAD1` (rev: `REV0`) and checkout new branch `BR1`
        # in `BR1` they both create a `filename.txt` , write their name into the file and commit (but not push) (commit ids `A1...` and `B1...`)
        # then they both run repo sync and we attempt to sync
        # When Alice pushes to the tracking repo, the `BR1` label will point to her commit
        # When Bob tries to run sync, he will get her branch and his commit will have to either override her (problematic to implement and unreliable)
        # or be atop of her commit (the shadow repo wont reflect the truth)
        # In conclusion, the "correct" way to do it is to create the internal branch (`T1` and `T2`)  and then "merge" the src branch into it
        # this will copy the shared commit tree from the src repo (upto and including `REV0`) and as it is pushed to the original repo, it will have the same order on both (even without the branch names)
        # due to the fact that commits are in an ordered tree
        # once the history upto `REV0` is merged (the commits ids are still the same) the un-pushed commit ids live only in the `T*` branches and on top of them
        # we are adding the sync commit
        # As we never merge between shadow branches the commit order of the src repository nor its Ids are ever changed
        # and the commit log of every shadow branch is synced_commit->un-pushed commits (to src)->pushed commits (to the src)
        if src.head.is_valid():
            tracking.git.merge('src/{}'.format(src.active_branch), allow_unrelated_histories=True)
            return True
        return False

    @classmethod
    def _push_to_tracking_repository_remote(cls, tracking_repository):
        if not tracking_repository.head.is_valid():
            tracking_repository.git.commit(m='empty commit', allow_empty=True)
        tracking_repository.remotes['origin'].push('{}:{}'.format(tracking_repository.active_branch, tracking_repository.active_branch))

    @classmethod
    def merge_src_to_tracking_repository(cls, src, tracking_repository, br_tag=None):
        git = import_git()
        if git.Remote(src, 'src') not in tracking_repository.remotes:
            tracking_repository.create_remote('src', src.git_dir)
        br_tag = br_tag or uuid.uuid4().hex[0:5]

        br_name = '{}_{}'.format(br_tag, src.active_branch)
        br_name = 'invocation/' + cls._sanitize_branch_name(br_name)
        cls._merge_to_new_branch(src, tracking_repository, br_name)
        cls._sync_uncommitted_changes(src, tracking_repository)
        cls._push_to_tracking_repository_remote(tracking_repository)
        cls._checkout(tracking_repository, 'dev_null')
        return br_name
