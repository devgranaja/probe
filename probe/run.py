import os
import asyncio
from probe.technology.config import Config
from probe.application.execution import create_probe, start_probe, stop_probe

from probe.technology.actions import probe_actions
from probe.technology.loader import actions


def load_configuration():
    cfg = Config()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(current_dir, 'technology', 'config.yml')
    print(fn)
    cfg.from_yaml(fn)
    return cfg

if __name__ == '__main__':

    configuration = load_configuration()

    loop = asyncio.get_event_loop()
    create_probe(configuration, actions, loop)
    start_probe()

    try:
        print("\n[ ---------- Running probe ---------- ]\n"
              "(Press CTRL-C to quit)\n")
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        # loop.run_until_complete(probe.cancel_tasks())
        stop_probe()
        loop.close()
