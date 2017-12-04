from probe.domain.probe import Probe

probe = None


async def create_probe(conf, act, repo, loop):
    global probe
    probe = Probe(conf, act, repo, loop)
    return probe


async def start_probe():
    print('\n[ -- Running {} ({}) -- ]\n'
          '(Press CTRL-C to quit)\n'.format(probe.name, probe.description))

    await probe.execute_tasks()


async def cancel_probe():
    await probe.cancel_tasks()


def get_configuration():
    return probe.configuration()