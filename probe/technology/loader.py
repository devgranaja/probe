import asyncio

actions = {}


def aaction(func):
    print('at decorator with ', func.__name__)
    if asyncio.iscoroutinefunction(func):
        actions[func.__name__] = func
    else:
        print('is not a async function')
        #raise(TypeError)
    return func
