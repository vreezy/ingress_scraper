from flask import Flask, request, send_from_directory
from flask import jsonify

app = Flask(__name__, static_url_path='', static_folder='',)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test/')
def test1():
    return app.send_static_file('response.json')

@app.route('/zone1/')
def zone1():
    response = app.send_static_file('response1.json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/zone2/')
def zone2():
    response =  app.send_static_file('response2.json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/zone3/')
def zone3():
    response =  app.send_static_file('response3.json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/zone4/')
def zone3():
    response =  app.send_static_file('response4.json')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
    #app.run(host="0.0.0.0", port=80)



