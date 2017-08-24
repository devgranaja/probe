from probe.technology.config import Config
import asyncio


def load_configuration():
    cfg = Config()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fn = os.path.join(current_dir, 'technology', 'config.yml')
    print(fn)
    cfg.from_yaml(fn)
    return cfg

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    p = Probe(conf, act, loop)
    start_probe(p)

    try:
        print("\n[ ---------- Running probe ---------- ]\n"
              "(Press CTRL-C to quit)\n")
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        # loop.run_until_complete(probe.cancel_tasks())
        probe.cancel_tasks()
        loop.close()
