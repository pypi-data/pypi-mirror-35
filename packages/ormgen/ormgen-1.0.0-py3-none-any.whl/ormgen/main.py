import argparse
import io
import sys

from ormgen import get_version
from ormgen.ormgen import OrmGenerator


def main():
    parser = argparse.ArgumentParser(add_help=False, description='Generates SQLAlchemy model code from an existing database.')
    parser.add_argument('--help', action='store_true', help="show help")
    parser.add_argument('-v', '--version', action='store_true', help="show version")
    parser.add_argument('-h', '--host', help='mysql host')
    parser.add_argument('-u', '--user', help='username')
    parser.add_argument('-p', '--password', help="password")
    parser.add_argument('-s', '--schema', help='schema')
    parser.add_argument('-o', '--outfile', help='file to write output to (default: stdout)')
    args = parser.parse_args()

    if args.help:
        parser.print_help()
        return
    if args.version:
        print(get_version())
        return
    if not args.host:
        print('You must supply a mysql host', file=sys.stderr)
        parser.print_help()
        return
    if not args.user:
        print('You must supply a username', file=sys.stderr)
        parser.print_help()
        return
    if not args.password:
        print('You must supply a password', file=sys.stderr)
        parser.print_help()
        return
    if not args.schema:
        print('You must supply a schema', file=sys.stderr)
        parser.print_help()
        return

    # Write the generated model code to the specified file or standard output
    outfile = io.open(args.outfile, 'wt', encoding='utf-8') if args.outfile else sys.stdout
    generator = OrmGenerator(args.host, args.user, args.password, args.schema)
    generator.render(outfile)

if __name__ == '__main__':
    main()
