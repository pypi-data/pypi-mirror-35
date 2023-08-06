import asyncio
import argparse
import random

import aiodns


class Resolver:
    def __init__(self, rate=100, coroutines=20, nameservers=None):
        self.coroutines = coroutines
        self.interval = 1.0/rate
        self.nameservers = nameservers or ["1.1.1.1"]

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("domains", type=argparse.FileType('r'),
                        help="File containing domains to resolve")
    args = parser.parse_args()

    with args.domains:
        domains = [line.strip() for line in args.domains]

    nameservers = ['1.1.1.1', '8.8.8.8', '8.8.4.4', '208.67.222.222', '208.67.220.220', '208.67.222.220', '208.67.220.222', '156.154.70.5', '156.154.71.5']

    resolver = Resolver(rate=1000, coroutines=18, nameservers=nameservers)
    print('\n'.join("{} => {}".format(x, y) for x, y in resolver.resolve_hosts(domains)))
