from probe.technology.loader import action


@action
async def simple_aaction():
    print('my first action')


def no_decorated_function():
    print('I am not a action')
