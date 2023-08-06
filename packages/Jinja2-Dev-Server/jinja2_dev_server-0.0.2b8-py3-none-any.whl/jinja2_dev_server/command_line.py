import argparse

from . import server


def main():
    parser = argparse.ArgumentParser(
        description='Runs a Flask-based Jinja2 development server')
    parser.add_argument('dirs', metavar='dir', type=str, nargs='+', default="./",
                        help='directory to be parsed. Defaults to \.')

    args = parser.parse_args()

    args = parser.parse_args()
    dirs = args.dirs

    server.run_server(dirs)
