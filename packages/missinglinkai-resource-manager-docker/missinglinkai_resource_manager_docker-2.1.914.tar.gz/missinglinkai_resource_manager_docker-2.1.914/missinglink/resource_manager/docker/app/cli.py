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
    ConfigBuilder.create_parse_and_save(active_config, **kwargs)


@cli.command('run')
def mk_run():
    conf_path, loop = CliTools.load_config()
    active_config = get_active_config()
    ConfigBuilder.create_parse_and_save(active_config)  # used for configuration migration
    CliTools.run_server(active_config, loop)

#
# @cli.command('job')
# @click.option('job', '-j', '--job', required=True, help='Job to execute and exit')
# @config_params
# def mk_job(job=None, **kwargs):
#     conf_path, loop = CliTools.load_config()
#     active_config = get_active_config()
#     ConfigBuilder.create_parse_and_save(active_config, **kwargs)  # used for configuration migration
#     active_config.general.pull_job = job
#     active_config.general.save()
#     click.echo(f'Run job {active_config.general.pull_job}')
#     CliTools.run_server(active_config, loop)
#     active_config.general.pull_job = None
#     active_config.general.save()
#     click.echo("Done")
