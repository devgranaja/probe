from probe.domain.probe import Probe

probe = None


def create_probe(conf, act, loop):
    global probe
    probe = Probe(conf, act, loop)


def start_probe():
    tasks = probe.create_tasks()
    return tasks


def stop_probe():
    probe.cancel_tasks()