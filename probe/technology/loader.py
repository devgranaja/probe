actions = {}


def action(func):
    print('at decorator with ', func.__name__)
    actions[func.__name__] = func
    return func
