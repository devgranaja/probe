import asyncio


class Probe:

    def __init__(self, config, act, loop):
        if config and act:
            self._configuration = config
            self._actions = act
        else:
            raise ValueError("Probe settings must be defined")

        self._tasks = []
        self._loop = loop

    def create_tasks(self):
        for act in self._configuration['probe']['actions']:
            act_id = act['action_id']
            act_name = act['action_name']
            act_func = self._actions[act_name]
            self._taskerize(act_id, act_name, act_func)
        return self._tasks

    def cancel_tasks(self):
        pending = asyncio.Task.all_tasks()

        for task in pending:
            task.cancel()
            try:
                # We must await task to execute its cancellation
                # cancelled task raises a asyncio.CancelledError exception
                self._loop.run_until_complete(task)
            except asyncio.CancelledError:
                pass

    def _taskerize(self, id, name, action, periodicity=None):
        """Create a asyncio task from a action (function)"""
        if asyncio.iscoroutinefunction(action):
            # convert a coroutine to a task
            task = asyncio.ensure_future(action())
        else:
            # convert a function to a task
            task = asyncio.ensure_future(self._sync_to_async(action))
        self._tasks.append(task)

    async def _sync_to_async(self, action):
        await self._loop.run_in_executor(None, action)
