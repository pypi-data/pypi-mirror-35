import os
import json

import jinja2
from flask import Flask
from flask import request, render_template, send_from_directory

templates = {}
variables = {}

debug = False

app = Flask(__name__)

cwd = os.getcwd()


def run_server(dirs, variables_file, debug_opt):
    global debug
    debug = debug_opt
    if type(dirs) == str:
        dirs = [dirs]
    for directory in dirs:
        read_files(directory)

    read_variables(variables_file)
    start_flask_server(dirs)


def read_variables(variables_file):
    global variables
    if os.path.exists(variables_file):
        with open(variables_file) as f:
            variables = json.load(f)


def read_files(filedir):
    global debug
    if not filedir.startswith("/"):
        filedir = os.path.join(os.getcwd(), filedir)

    # r=root, d=directories, f = files
    for r, d, f in os.walk(filedir):
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


def start_flask_server(filedir):
    my_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader(filedir),
    ])
    app.jinja_loader = my_loader

    app.run(debug=True)


@app.route('/<path:path>')
def serve_template(path):
    if debug:
        print(path, path in templates)
    if path in templates:
        if os.path.exists(templates[path]):
            return render_template(templates[path], **variables)
        else:
            return send_from_directory(path)
    return 404
