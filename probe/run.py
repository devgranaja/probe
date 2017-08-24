import os
import signal
import asyncio
from probe.technology.config import Config
from probe.application.execution import create_probe,  start_probe, cancel_probe

from probe.technology.actions import probe_actions
from probe.technology.loader import actions


def load_configuration():
    cfg = Config()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(current_dir, 'technology', 'config.yml')
    cfg.from_yaml(fn)
    return cfg


def raise_system_exit():
    raise SystemExit

async def main(configuration, loop):
    await create_probe(configuration, actions, loop)
    await start_probe()
    try:
        pass
    except (SystemExit, KeyboardInterrupt):
        pass
    finally:
        print("\n[ ^^^ Closing probe ^^^]\n")
        await cancel_probe()


if __name__ == '__main__':
    configuration = load_configuration()
    loop = asyncio.get_event_loop()

    loop.add_signal_handler(signal.SIGINT, raise_system_exit)
    loop.add_signal_handler(signal.SIGTERM, raise_system_exit)

    loop.run_until_complete(main(configuration, loop))

    loop.close()