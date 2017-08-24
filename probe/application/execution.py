from probe.domain.probe import Probe

probe = None


def create_probe(conf, act, loop):
    global probe
    probe = Probe(conf, act, loop)
    tasks = probe.create_tasks()
    return tasks


def cancel_probe():
    probe.cancel_tasks()