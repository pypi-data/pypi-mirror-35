import argparse

from . import server


def main():
    parser = argparse.ArgumentParser(
        description='Runs a Flask-based Jinja2 development server')
    parser.add_argument('dirs', metavar='dir', type=str, nargs='?', default="./",
                        help='directory to be parsed. Defaults to \.')
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("--parameters", nargs='?', default="variables.json",
                        help="specify file containing jinja2 parameters")

    args = parser.parse_args()

    dirs = args.dirs

    server.run_server(dirs, args.parameters, args.verbose)
