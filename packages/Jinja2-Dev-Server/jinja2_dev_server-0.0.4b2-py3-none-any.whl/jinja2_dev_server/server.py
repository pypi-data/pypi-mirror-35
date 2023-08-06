import os
import json

import jinja2
from flask import Flask
from flask import request, render_template

templates = {}
variables = {}

debug = False

app = Flask(__name__)
my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader([os.getcwd()]),
])
app.jinja_loader = my_loader

cwd = os.getcwd()


def run_server(dirs, variables_file, debug_opt):
    global debug
    debug = debug_opt
    if type(dirs) == str:
        dirs = [dirs]
    for directory in dirs:
        read_files(directory)

    read_variables()
    start_flask_server()


def read_variables(variables_file):
    global variables
    if os.path.exists(variables_dir):
        with open(variables_dir) as f:
            variables = json.load(f)


def read_files(dir):
    global debug
    thisdir = os.getcwd()

    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        for file in f:
            if debug:
                print(file)
            if ".jinja2" in file:
                if debug:
                    print("Found " + file)

                filepath = os.path.join(r, file)

                templates[file[:file.find(".")]] = filepath[len(cwd) + 1:]

    if len(templates) == 0:
        raise Exception("No files found")
    if debug:
        print(templates)


def start_flask_server():
    app.run(debug=True)


@app.route('/<path:path>')
def serve_template(path):
    if debug:
        print(path, path in templates)
    if path in templates:
        return render_template(templates[path], **variables)
    return 404
