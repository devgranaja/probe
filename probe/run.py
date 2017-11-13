import os
import sys
from aiohttp import web
from probe.technology.config import Config
from probe.technology.text_file_repository import TextFileRepository
from probe.application.interactor import create_probe,  start_probe, cancel_probe

from probe.technology.actions import probe_actions
from probe.domain.taskerize import actions


def load_configuration():
    cfg = Config()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(current_dir, 'technology', 'config.yml')
    cfg.from_yaml(fn)
    return cfg


async def start(loop):
    configuration = load_configuration()
    repository = TextFileRepository('technology/logs/dataprobe.log')

    await create_probe(configuration, actions, repository, loop)
    #try:
    await start_probe()
    #finally:
        #await cancel_probe()

async def close():
    print("\n[ ^^^ Closing probe ^^^]\n")
    await cancel_probe()

async def handler(request):
    response = {'status': 'success'}
    return web.json_response(response)
    #return web.Response(text="Hello, world")

async def startup_background_tasks(app):
    app['startup_probe'] = app.loop.create_task(start(app.loop))

async def cleanup_background_tasks(app):
    app['cleanup_probe'] = app.loop.create_task(close)

def init(argv):
    app = web.Application()

    app.on_startup.append(startup_background_tasks)
    #app.on_cleanup.append(cleanup_background_tasks)

    app.router.add_get('/', handler)

    web.run_app(app)


if __name__ == '__main__':
    init(sys.argv)

