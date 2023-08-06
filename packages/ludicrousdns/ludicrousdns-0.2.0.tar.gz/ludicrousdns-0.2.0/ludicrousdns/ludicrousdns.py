import asyncio
from asyncio import FIRST_COMPLETED
import os

import aiodns

from .util import ClosableQueue, QueueClosed, read_nameservers_from_file


Token = 1


class ResolverWorker:
    def __init__(self, loop, nameserver):
        self._resolver = aiodns.DNSResolver(loop=loop, nameservers=[nameserver])
        self._token_queue = asyncio.Queue()

        rate = 100  # per second
        self._interval = 1/rate
        self._coroutines = 10

    async def _query(self, name):
        for query_type in ["CNAME", "A", "AAAA"]:
            try:
                await self._token_queue.get()
                resp = await self._resolver.query(name, query_type)
                if query_type == "CNAME":
                    return resp.cname
                return resp[0].host
            except (aiodns.error.DNSError, UnicodeError, IndexError):
                continue

        return None

    async def _worker(self, queue, outqueue):
        while True:
            try:
                host = await queue.get()
            except QueueClosed:
                break
            resolved = await self._query(host)
            if resolved:
                await outqueue.put((host, resolved))

    async def _feed_tokens(self):
        while True:
            await self._token_queue.put(Token)
            await asyncio.sleep(self._interval)

    async def resolve_from_queue(self, queue, outqueue):
        token_feeder = asyncio.ensure_future(self._feed_tokens())
        workers = [self._worker(queue, outqueue) for _ in range(self._coroutines)]

        await asyncio.wait([token_feeder, asyncio.gather(*workers)], return_when=FIRST_COMPLETED)
        token_feeder.cancel()


class Resolver:
    def __init__(self, nameservers=None):
        if not nameservers:
            current_dir = os.path.dirname(os.path.realpath(__file__))
            nameservers = read_nameservers_from_file(current_dir + "/data/nameservers.txt")

        self.loop = asyncio.get_event_loop()
        self.resolvers = []
        for ns in nameservers:
            self.resolvers.append(ResolverWorker(self.loop, ns))

        self._host_queue = ClosableQueue()

    async def _feed_hosts(self, hosts):
        for host in hosts:
            await self._host_queue.put(host)

        self._host_queue.close()

    async def _resolve_hosts(self, hosts):
        outqueue = asyncio.Queue()
        resolver_futures = []
        for resolver in self.resolvers:
            resolver_futures.append(resolver.resolve_from_queue(self._host_queue, outqueue))

        await asyncio.gather(self._feed_hosts(hosts), *resolver_futures)

        return list(outqueue._queue)  # pylint: disable=protected-access

    def resolve_hosts(self, hosts):
        return self.loop.run_until_complete(self._resolve_hosts(hosts))
