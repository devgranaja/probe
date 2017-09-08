from probe.domain.taskerize import action


@action
async def simple_action():
    print('my first action')


def no_decorated_function():
    print('I am not a action')
