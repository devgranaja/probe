from probe.domain.probe import Probe

probe = None


async def create_probe(conf, act, loop):
    global probe
    probe = Probe(conf, act, loop)
    return probe


async def start_probe():
    print('\n[ -- Running {} ({}) -- ]\n'
          '(Press CTRL-C to quit)\n'.format(probe.name, probe.description))

    await probe.execute_tasks()


async def cancel_probe():
    await probe.cancel_tasks()