#!/usr/bin/env python
# -*- coding: utf8 -*-
import logging
import os
import re
import sys
import click
import warnings
from missinglink_commands.http_session import create_http_session
from missinglink_commands.legit.config import default_missing_link_folder
from missinglink_commands.legit.context import init_context2
from missinglink_commands.legit.exceptions import MissingLinkException
from missinglink_commands.legit.gcp_services import GooglePackagesMissing, GoogleAuthError
from missinglink_commands.legit.path_utils import makedir
from missinglink_commands.mali_version import get_missinglink_cli_version, get_missinglink_package
from self_update.sdk_version import get_keywords
import click_completion

__prev_resolve_ctx = click_completion.resolve_ctx


def __mali_resolve_ctx(_cli, prog_name, args):
    def find_top_parent_ctx(current_ctx):
        parent = current_ctx
        while True:
            if current_ctx.parent is None:
                break

            parent = current_ctx.parent
            current_ctx = parent

        return parent

    ctx = __prev_resolve_ctx(cli, prog_name, args)

    top_ctx = find_top_parent_ctx(ctx)

    init_context2(
        ctx,
        top_ctx.params.get('session'),
        top_ctx.params.get('output_format'),
        top_ctx.params.get('config_prefix'),
        top_ctx.params.get('config_file'))

    return ctx


click_completion.resolve_ctx = __mali_resolve_ctx
click_completion.init()


def token_normalize_func(token):
    convert = {
        'projectId': 'project',
        'project-Id': 'project',
        'experimentId': 'experiment',
        'experiment-id': 'experiment',
        'no_progressbar': 'no-progressbar',
        'noProgressbar': 'no-progressbar',
        'enable_progressbar': 'enable-progressbar',
        'enableProgressbar': 'enable-progressbar'
    }

    def is_camel(s):
        return s != s.lower() and s != s.upper() and "_" not in s

    def convert_camel_case(name):
        s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1-\2', name)
        return re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', s1).lower()

    new_token = convert.get(token)

    if new_token is None and is_camel(token):
        new_token = convert_camel_case(token)

    if new_token is not None and not os.environ.get('ML_DISABLE_DEPRECATED_WARNINGS'):
        click.echo('"%s" is deprecated use "%s" instead' % (token, new_token), err=True)

    return new_token or token


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'], color=True, token_normalize_func=token_normalize_func)


def _setup_logger(log_level):
    if not log_level:
        return

    log_level = log_level.upper()

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%dT%H:%M:%S')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    logging_method = getattr(root_logger, log_level.lower())
    logging_method('log level set to %s (this is a test message)', log_level)


class Choice2(click.ParamType):
    """The choice type allows a value to be checked against a fixed set of
    supported values.  All of these values have to be strings.
    :param case_sensitive: Set to false to make choices case insensitive.
    Defaults to true.
    See :ref:`choice-opts` for an example.
    """
    name = 'choice2'

    def __init__(self, choices, case_sensitive=False):
        self.choices = choices
        self.case_sensitive = case_sensitive

    def get_metavar(self, param):
        return '[%s]' % '|'.join(self.choices)

    def get_missing_message(self, param):
        return 'Choose from %s.' % ', '.join(self.choices)

    def _normalize_value(self, ctx, value):
        # Match through normalization and case sensitivity
        # first do token_normalize_func, then lowercase
        # preserve original `value` to produce an accurate message in
        # `self.fail`
        if ctx is not None and ctx.token_normalize_func is not None:
            normed_value = ctx.token_normalize_func(value)
            normed_choices = [ctx.token_normalize_func(choice) for choice in self.choices]
        else:
            normed_value = value
            normed_choices = self.choices

        return normed_value, normed_choices

    def _get_normed_choices_value(self, ctx, value):
        normed_value, normed_choices = self._normalize_value(ctx, value)

        if not self.case_sensitive:
            normed_value = normed_value.lower()
            normed_choices = [choice.lower() for choice in normed_choices]

        return normed_value, normed_choices

    def convert(self, value, param, ctx):
        # Exact match
        if value in self.choices:
            return value

        normed_value, normed_choices = self._get_normed_choices_value(ctx, value)

        if normed_value in normed_choices:
            return normed_value

        self.fail('invalid choice: %s. (choose from %s)' % (value, ', '.join(self.choices)), param, ctx)

    def __repr__(self):
        return 'Choice(%r)' % list(self.choices)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--output-format', '-o', type=Choice2(['tables', 'json', 'csv', 'json-lines']), default='tables', required=False)
@click.option('--config-prefix', '-cp', envvar='ML_CONFIG_PREFIX', required=False)
@click.option('--config-file', '-cf', envvar='ML_CONFIG_FILE', required=False)
@click.option('--log-level', envvar='ML_LOG_LEVEL', type=Choice2(['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']), required=False)
@click.pass_context
def cli(ctx, output_format, config_prefix, config_file, log_level):
    from tqdm import TqdmSynchronisationWarning

    warnings.filterwarnings('ignore', category=TqdmSynchronisationWarning)

    _setup_logger(log_level)
    init_context2(ctx, create_http_session(), output_format, config_prefix, config_file)


@cli.command()
@click.argument('shell', required=False, type=click_completion.DocumentedChoice(click_completion.shells))
def install(shell):
    """Install the click-completion-command completion"""
    from missinglink_commands.install import rc_updater

    shell = shell or click_completion.get_auto_shell()

    code = click_completion.get_code(shell)

    file_name = '{dir}/completion.{shell}.inc'.format(dir=default_missing_link_folder(), shell=shell)

    makedir(file_name)

    with open(file_name, 'w') as f:
        f.write(code)

    rc_updater(shell, file_name)


@cli.command('version')
@click.pass_context
def version(_ctx):
    current_version = get_missinglink_cli_version()

    click.echo(current_version)


# noinspection PyBroadException
def update_sdk(latest_version, user_path, throw_exception):
    from self_update.pip_util import pip_install, get_pip_server

    keywords = get_keywords(get_missinglink_package()) or []

    require_package = '%s==%s' % (get_missinglink_package(), latest_version)
    p, args = pip_install(get_pip_server(keywords), require_package, user_path)

    if p is None:
        return False

    try:
        std_output, std_err = p.communicate()
    except Exception:
        if throw_exception:
            raise

        logging.exception("%s failed", " ".join(args))
        return False

    rc = p.returncode

    if rc != 0:
        logging.error('%s failed to upgrade to latest version (%s)', get_missinglink_package(), latest_version)
        logging.error("failed to run %s (%s)\n%s\n%s", " ".join(args), rc, std_err, std_output)
        return False

    logging.info('%s updated to latest version (%s)', get_missinglink_package(), latest_version)

    return True


def self_update(throw_exception=False):
    from self_update.pip_util import get_latest_pip_version

    current_version = get_missinglink_cli_version()
    keywords = get_keywords(get_missinglink_package()) or []

    if current_version is None:
        return

    latest_version = get_latest_pip_version(get_missinglink_package(), keywords, throw_exception=throw_exception)

    if latest_version is None:
        return

    if current_version == latest_version:
        return

    running_under_virtualenv = getattr(sys, 'real_prefix', None) is not None

    if not running_under_virtualenv:
        logging.info('updating %s to version %s in user path', get_missinglink_package(), latest_version)

    return update_sdk(latest_version, user_path=not running_under_virtualenv, throw_exception=throw_exception)


def add_commands():
    from missinglink_commands import auth_commands, projects_commands, orgs_commands, experiments_commands, code_commands, \
        models_commands, data_commands, run_commands, resource_commands, aws_commands, defaults_commands

    cli.add_command(auth_commands)
    cli.add_command(projects_commands)
    cli.add_command(orgs_commands)
    cli.add_command(aws_commands)
    cli.add_command(experiments_commands)
    cli.add_command(code_commands)
    cli.add_command(models_commands)
    cli.add_command(data_commands)
    cli.add_command(run_commands)
    cli.add_command(resource_commands)
    cli.add_command(defaults_commands)


def main():
    import os
    if sys.argv[0].endswith('/mali') and not os.environ.get('ML_DISABLE_DEPRECATED_WARNINGS'):
        click.echo('instead of mali use ml (same tool with a different name)')

    if os.environ.get('MISSINGLINKAI_ENABLE_SELF_UPDATE'):
        self_update()

    add_commands()
    cli()


if __name__ == "__main__":
    try:
        main()
    except GooglePackagesMissing:
        click.echo('you to run "pip install missinglink[gcp]" in order to run this command', err=True)
    except GoogleAuthError:
        click.echo('Google default auth credentials not found, run gcloud auth application-default login', err=True)
    except MissingLinkException as ex:
        click.echo(ex, err=True)
