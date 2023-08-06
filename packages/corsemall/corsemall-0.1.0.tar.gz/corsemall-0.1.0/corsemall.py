"""
Serves JSON data with CORS allowed from *.json files at given path.
"""
import json
import os
import sys

from flask import Flask, render_template_string, jsonify

app = Flask(__name__)
INDEX = '''<html><head><title>CORS all</title></head>
<body>
<h1> INDEX of *.json files at {{ path }}:</h1>
  <ul>
    {% for file in files %}
    <li><a href="/{{ file }}">{{ file }}</a></li>
    {% endfor %}
  </ul>
</body>
</html>
'''


@app.route('/')
def index():
    path = os.path.abspath(os.environ.get('CORSALL_PATH', '.'))
    files = [fn for fn in os.listdir(path) if fn.endswith('.json')]

    return render_template_string(INDEX, path=path, files=files)


@app.route('/<string:page>')
def return_with_cors_enabled(page):
    base_path = os.path.abspath(os.environ.get('CORSALL_PATH', '.'))
    page_path = os.path.join(base_path, page)
    with open(page_path) as f:
        data = json.load(f)
        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


def cli():
    try:
        path = sys.argv[1]
    except IndexError:
        pass
    else:
        os.environ['CORSALL_PATH'] = path
    app.run(debug=True)


if __name__ == "__main__":
    cli()
