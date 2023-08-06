import argparse

from . import Resolver, read_nameservers_from_string


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nameservers", type=argparse.FileType('r'),
                        help="File containing nameservers to connect to")
    parser.add_argument("domains", type=argparse.FileType('r'),
                        help="File containing domains to resolve")
    args = parser.parse_args()

    with args.domains:
        domains = [line.strip() for line in args.domains]

    if args.nameservers:
        with args.nameservers:
            nameservers = read_nameservers_from_string(args.nameservers.read())
        resolver = Resolver(nameservers)
    else:
        resolver = Resolver()

    print('\n'.join("{} => {}".format(x, y) for x, y in resolver.resolve_hosts(domains)))
