from flask import Flask, request, send_from_directory
from flask import jsonify

app = Flask(__name__, static_url_path='', static_folder='',)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
    #app.run(host="0.0.0.0", port=80)