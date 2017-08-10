import asyncio


class Probe:

    def __init__(self):
        self.tasks = []
        self.loop = asyncio.get_event_loop()

    def taskerize(self, id, name, action, periodicity=None):
        """Create a asyncio task from a action (function)"""
        if asyncio.iscoroutinefunction(action):
            task = asyncio.ensure_future(action())
        else:
            task = asyncio.ensure_future(self._sync_to_async(action))
            #task = asyncio.run_in_executor(None, action)
        self.tasks.append(task)

    def _sync_to_async(self, action):
        """Create a async coroutine from a non async function"""
        async def _to_async():
            await asyncio.run_in_executor(None, action)

        return _to_async
