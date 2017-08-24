from probe.domain.probe import Probe

probe = None


async def create_probe(conf, act, loop):
    global probe
    probe = Probe(conf, act, loop)


async def start_probe():
    await probe.execute_tasks()


async def cancel_probe():
    await probe.cancel_tasks()