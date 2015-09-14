import sys, os
import json
from flask import Flask, request, url_for, render_template

@app.route('/images')
def index():
    with open("sample.json") as json_file:
		d = json.load(json_file)
		return d
    return Response(json_file, mimetype='application/json')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)