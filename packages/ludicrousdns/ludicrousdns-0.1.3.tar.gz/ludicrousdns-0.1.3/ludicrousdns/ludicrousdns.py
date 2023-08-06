import asyncio
import os
import random
import re

import aiodns


def read_resolvers_from_file(filename):
    with open(filename) as f:
        resolvers = [re.sub(r'#.*$', '', line).strip() for line in f]
    return [r for r in resolvers if r != '']


class Resolver:
    def __init__(self, rate=100, coroutines=20, nameservers=None):
        self.coroutines = coroutines
        self.interval = 1.0/rate

        if not nameservers:
            current_dir = os.path.dirname(os.path.realpath(__file__))
            nameservers = read_resolvers_from_file(current_dir + "/data/resolvers.txt")

        self.nameservers = nameservers

        self.loop = asyncio.get_event_loop()
        self.resolvers = []
        for ns in self.nameservers:
            self.resolvers.append(aiodns.DNSResolver(loop=self.loop, nameservers=[ns]))

        self.queue = asyncio.Queue()
        self.result = []

    async def query(self, name):
        for query_type in ["CNAME", "A", "AAAA"]:
            try:
                resolver = random.choice(self.resolvers)
                resp = await resolver.query(name, query_type)
                if query_type == "CNAME":
                    return resp.cname
                return resp[0].host
            except (aiodns.error.DNSError, UnicodeError, IndexError):
                continue

        return None

    async def _feeder(self, hosts):
        for host in hosts:
            await self.queue.put(host)
            await asyncio.sleep(self.interval)

        for _ in range(self.coroutines):
            await self.queue.put(None)

    async def _resolver(self):
        while True:
            q = await self.queue.get()
            if q is None:
                break
            host = await self.query(q)
            if host:
                self.result.append((q, host))

    async def _resolve(self, hosts):
        feeder = self._feeder(hosts)
        resolvers = asyncio.gather(*[self._resolver() for _ in range(self.coroutines)])

        await asyncio.gather(feeder, resolvers)

        return self.result

    def resolve_hosts(self, hosts):
        return self.loop.run_until_complete(self._resolve(hosts))
