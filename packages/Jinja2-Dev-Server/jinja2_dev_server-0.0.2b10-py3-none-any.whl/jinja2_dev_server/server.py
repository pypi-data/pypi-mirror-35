import os

from flask import Flask
from flask import request, render_template

templates = {}


def run_server(dirs):
    for directory in dirs:
        read_files(directory)

    start_flask_server()


def read_files(dir):
    thisdir = os.getcwd()

    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        for file in f:
            if ".jinja2" in file:
                print(os.path.join(r, file))
                templates[:file.index(".")] = os.path.join(r, file)

    print(templates)


def start_flask_server():
    app = Flask(__name__)

    @app.route('{template}')
    def serve_template():
        template = request.match_info['user']
        if template in templates:
            return render_template(templates[template])
        return 404
