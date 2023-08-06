import os

from flask import Flask
from flask import request, render_template

templates = {}

debug = False

app = Flask(__name__, template_folder=".")


def run_server(dirs, debug_opt):
    global debug
    debug = debug_opt
    if type(dirs) == str:
        dirs = [dirs]
    for directory in dirs:
        read_files(directory)

    start_flask_server()


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
                templates[file[:file.find(".")]] = os.path.join(d, file)

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
        return render_template(templates[path])
    return 404
