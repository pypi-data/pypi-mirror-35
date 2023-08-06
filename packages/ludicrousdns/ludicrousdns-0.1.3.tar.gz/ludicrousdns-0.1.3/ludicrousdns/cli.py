import argparse

from .ludicrousdns import Resolver


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("domains", type=argparse.FileType('r'),
                        help="File containing domains to resolve")
    args = parser.parse_args()

    with args.domains:
        domains = [line.strip() for line in args.domains]

    resolver = Resolver(rate=1000, coroutines=18)
    print('\n'.join("{} => {}".format(x, y) for x, y in resolver.resolve_hosts(domains)))
