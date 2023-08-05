import asyncio
from typing import (  # noqa: F401
    Any,
    AsyncIterable,
    Callable,
    Dict,
    List,
    Optional,
    Type,
    cast,
)
import uuid

import aioprocessing

from .misc import (
    BaseEvent,
    BroadcastConfig,
    Subscription,
)


class Endpoint:

    def __init__(self,
                 name: str,
                 sending_queue: aioprocessing.AioQueue,
                 receiving_queue: aioprocessing.AioQueue) -> None:

        self.name = name
        self._sending_queue = sending_queue
        self._receiving_queue = receiving_queue
        self._futures: Dict[str, asyncio.Future] = {}
        self._handler: Dict[Type[BaseEvent], List[Callable[[BaseEvent], Any]]] = {}
        self._queues: Dict[Type[BaseEvent], List[asyncio.Queue]] = {}

    def broadcast(self, item: BaseEvent, config: Optional[BroadcastConfig] = None) -> None:
        item._origin = self.name
        self._sending_queue.put_nowait((item, config))

    async def request(self, item: BaseEvent) -> BaseEvent:
        item._origin = self.name
        item._id = str(uuid.uuid4())

        future: asyncio.Future = asyncio.Future()
        self._futures[item._id] = future

        self._sending_queue.put_nowait((item, None))

        result = await future

        return cast(BaseEvent, result)

    def connect(self) -> None:
        asyncio.ensure_future(self._connect())

    async def _connect(self) -> None:
        while True:
            (item, config) = await self._receiving_queue.coro_get()
            has_config = config is not None

            event_type = type(item)
            in_futures = has_config and config.filter_event_id in self._futures
            in_queue = event_type in self._queues
            in_handler = event_type in self._handler

            if not in_queue and not in_handler and not in_futures:
                continue

            if in_futures:
                future = self._futures[config.filter_event_id]
                future.set_result(item)
                self._futures.pop(config.filter_event_id)

            if in_queue:
                for queue in self._queues[event_type]:
                    queue.put_nowait(item)

            if in_handler:
                for handler in self._handler[event_type]:
                    handler(item)

    def subscribe(self,
                  event_type: Type[BaseEvent],
                  handler: Callable[[BaseEvent], None]) -> Subscription:

        if event_type not in self._handler:
            self._handler[event_type] = []

        self._handler[event_type].append(handler)

        return Subscription(lambda: self._handler[event_type].remove(handler))

    async def stream(self, event_type: Type[BaseEvent]) -> AsyncIterable[BaseEvent]:
        queue: asyncio.Queue = asyncio.Queue()

        if event_type not in self._queues:
            self._queues[event_type] = []

        self._queues[event_type].append(queue)

        while True:
            event = await queue.get()
            try:
                yield event
            except GeneratorExit:
                self._queues[event_type].remove(queue)
