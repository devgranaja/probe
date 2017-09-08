import asyncio
import math


class Probe:

    def __init__(self, config, act):
        if config and act:
            self._configuration = config
            self._actions = act
        else:
            raise ValueError("Probe settings must be defined")

        self.name = self._configuration['probe']['probe_name']
        self.description = self._configuration['probe']['probe_description']

        self._all_tasks = None

    async def execute_tasks(self):

        tasks = []
        for act in self._configuration['probe']['actions']:
            items = act['items']
            if act['iterations'] == '.inf':
                iterations = math.inf
            else:
                iterations = act['iterations']
            period = act['period']
            tasks.append(self._actions[act['action_name']](items, iterations, period))

        self._all_tasks = asyncio.gather(*tasks)
        await self._all_tasks

# TODO review the cancel_tasks procedure. Do we have to catch the asyncio.CancelledError exception at coro ?
    async def cancel_tasks(self):
            self._all_tasks.cancel()
            try:
                # We must await task to execute its cancellation
                # cancelled task raises a asyncio.CancelledError exception
                await self._all_tasks
            except asyncio.CancelledError:
                pass