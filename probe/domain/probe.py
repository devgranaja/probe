import asyncio


class Probe:

    def __init__(self, config=None, act=None):
        if config and act:
            self._configuration = config
            self._actions = act
        else:
            raise ValueError("Probe settings must be defined")

        self.tasks = []
        self._loop = asyncio.get_event_loop()

    def create_tasks(self):
        for act in self._configuration['probe']['actions']:
            act_id = act['action_id']
            act_name = act['action_name']
            act_func = self._actions[act_name]
            self._taskerize(act_id, act_name, act_func)

    def _taskerize(self, id, name, action, periodicity=None):
        """Create a asyncio task from a action (function)"""
        if asyncio.iscoroutinefunction(action):
            # convert a coroutine to a task
            task = asyncio.ensure_future(action())
        else:
            # convert a function to a task
            task = asyncio.ensure_future(self._sync_to_async(action))
        self.tasks.append(task)

    async def _sync_to_async(self, action):
        await asyncio.run_in_executor(None, action)
