import logging

log = logging.getLogger(__name__)

actions = {}


def action(func):
    actions[func.__name__] = func
    log.debug('Action {} registered.'.format(func.__name__))
    return func
