import click

from missinglink.resource_manager.docker.controllers.configuration import get_active_config
from .cli_tools import CliTools
from .config_builder import ConfigBuilder, config_params


@click.group(help='Missing Link Resource Manager version#%s' % CliTools.get_version())
def cli():
    pass


@cli.command('version')
def print_version():
    click.echo(CliTools.get_version())


@cli.command('config')
@config_params
def mk_config(**kwargs):
    CliTools.load_config()
    active_config = get_active_config()
    ConfigBuilder.create(active_config, **kwargs).parse_and_save()


@cli.command('run')
def mk_run():
    CliTools.run_ws()
