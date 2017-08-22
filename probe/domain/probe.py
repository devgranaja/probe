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

    def execute_tasks(self):
        group = asyncio.gather(*self.tasks)
        results = self._loop.run_until_complete(group)
        print('Execution results: {}'.format(results))
        #self._loop.run_until_complete(self.tasks[0])
        #t = asyncio.ensure_future(self.miprint())
        #self._loop.run_until_complete(t)
        #a = self._actions['async_sleep']
        #print(futures.isfuture(a))
        #print(asyncio.iscoroutine(a()))
        #print(asyncio.iscoroutinefunction(a))
        #self._loop.run_until_complete(a())
        #print(self._actions)


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
        await self._loop.run_in_executor(None, action)

    async def miprint(self):
        print("mio")
