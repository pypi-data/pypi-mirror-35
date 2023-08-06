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
dirs = ["./"]


def run_server(dirs_opt, variables_file, debug_opt):
    global debug
    global dirs
    debug = debug_opt
    if typeof(dirs, str):
        dirs_opt = [dirs_opt]
    dirs = dirs_opt
    if debug:
        print(dirs)
    for directory in dirs:
        read_files(directory)

    read_variables(variables_file)
    start_flask_server()


def read_variables(variables_file):
    global variables
    if os.path.exists(variables_file):
        with open(variables_file) as f:
            variables = json.load(f)


def read_files(filedir, prefix=""):
    global debug
    if not filedir.startswith("/"):
        filedir = os.path.join(os.getcwd(), filedir)

    if debug:
        print(filedir)

    # r=root, d=directories, f = files
    for r, d, f in os.walk(filedir):
        for file in f:
            if debug:
                print(file)
            if ".jinja2" in file:
                if debug:
                    print("Found " + file)

                filepath = os.path.join(r, file)

                templpath = os.path.join(prefix, file[:file.find(".")])

                templates[templpath] = filepath[len(filedir) + 1:]

    if len(templates) == 0:
        raise Exception("No files found")
    if debug:
        print(templates)


def start_flask_server():
    global dirs
    my_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader(dirs),
    ])
    app.jinja_loader = my_loader
    print(dirs)

    app.run(debug=True)


@app.route('/<path:path>')
def serve_template(path):
    global dirs
    filename = path[path.rfind("/") + 1:]
    filedir = path[:path.rfind("/") + 1]

    if debug:
        print(path, path in templates)
    if path in templates:
        # HEY GUESS WHAT THIS IS RELATIVE TO CURRENT NOT TO TEMPLATE DIRECTORY YOU GENIUS
        for directory in dirs:
            if os.path.exists(os.path.join(directory, templates[path])):
                return render_template(templates[path], **variables)
        else:
            return send_from_directory(filedir, filename)
    return 404
