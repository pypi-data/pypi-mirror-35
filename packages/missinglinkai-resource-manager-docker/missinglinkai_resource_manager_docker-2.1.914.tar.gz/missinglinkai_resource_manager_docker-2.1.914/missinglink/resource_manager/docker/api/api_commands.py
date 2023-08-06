import asyncio
import functools
import json
import logging

from missinglink.resource_manager.docker.controllers import DockerWrapper
from .docker_execution import DockerExecution

logger = logging.getLogger(__name__)


class CommandResponseError(Exception):
    def __init__(self, command, response):
        self.command = command
        self.response = response


async def send_command(send, command_name, command_version, **kwargs):
    await send(command=f"{command_name}:{command_version}", data=kwargs)


async def register_1(send, active_config, **kwargs):
    data = DockerWrapper.get().be_summary()
    data["gpu_present"] = DockerWrapper.get().has_nvidia()
    data["pull_job"] = active_config.general.pull_job
    if active_config.general.get('hostname'):
        data['server'] = data.get('server', {})
        data['server']['name'] = active_config.general.get('hostname')

    logger.info(data)
    response = await send(command="REGISTER:1", jwt=active_config.general.jwt, data=data, rpc=True)

    if response.get('ok', False):
        logger.info("Connected")
        return True
    raise CommandResponseError("register_1", response)


running_tasks = {}


def remove_completed_task(t_id, task):
    res = running_tasks.pop(t_id, None)
    if res is not None:
        print(f'invocation Id {t_id} completed')


async def kill_1(send, active_config, **kwargs):
    invocation_id = kwargs['invocation_id']
    task = running_tasks.pop(invocation_id, None)
    logger.info(f'Killing {invocation_id}: {task}')
    if task is None:
        return

    task.cancel()


async def running_1(send, active_config, **kwargs):
    tasks = dict(running_tasks)
    return {'ok': tasks}


async def run_1(send, active_config, **kwargs):
    logger.info('RUN_1: %s', json.dumps(kwargs))
    kwargs['active_config'] = active_config
    invocation_id = kwargs['invocation_id']

    task = asyncio.ensure_future(DockerExecution.create(send, **kwargs).run_manged())
    task.add_done_callback(functools.partial(remove_completed_task, invocation_id))
    logger.info(f'{invocation_id} is now running')
    running_tasks[invocation_id] = task
    return {'ok': True, 'invocation_id': invocation_id}


async def echo_1(send, active_config, **kwargs):
    logger.info('echo_1: %s', json.dumps(kwargs))
    return kwargs


async def on_connect(send, active_config, **kwargs):
    logger.debug('on_connect %s %s', active_config, kwargs)
    await send(jwt=active_config.general.jwt)


API_MAPPING = {
    'REGISTER:1': register_1,
    'RUN:1': run_1,
    'KILL:1': kill_1,
    '_on_connect': on_connect
}
