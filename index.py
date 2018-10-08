from flask import Flask, jsonify
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def index():
    return "Hello There!"

@app.route('/<name>')
def get_name(name):
    return 'Hello {}!'.format(name)

@app.route('/data')
def names():
    data = {"Names": ["Anna", "Joanna", "Thomas", "CK", "John"]}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
