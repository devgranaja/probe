import asyncio


class Probe:

    def __init__(self, config, act, loop):
        if config and act:
            self._configuration = config
            self._actions = act
        else:
            raise ValueError("Probe settings must be defined")

        self.name = self._configuration['probe']['probe_name']
        self.description = self._configuration['probe']['probe_description']

        self._tasks = []
        self._loop = loop
        self._all_tasks = None

        self.create_tasks()

    def create_tasks(self):
        for act in self._configuration['probe']['actions']:
            act_id = act['action_id']
            act_name = act['action_name']
            act_func = self._actions[act_name]
            act_periodicity = act['periodicity']
            self._taskerize(act_id, act_name, act_func, act_periodicity)

    async def execute_tasks(self):
        self._all_tasks = asyncio.gather(*self._tasks)
        await self._all_tasks

    async def cancel_tasks(self):
            self._all_tasks.cancel()
            try:
                # We must await task to execute its cancellation
                # cancelled task raises a asyncio.CancelledError exception
                await self._all_tasks
            except asyncio.CancelledError:
                pass

    def _taskerize(self, id, name, action, periodicity=None):
        """Create a asyncio task from a action (asyncio function)"""
        if periodicity is None:
            period = 0
        else:
            period = periodicity * 60

        task = asyncio.ensure_future(action(period))
        self._tasks.append(task)

