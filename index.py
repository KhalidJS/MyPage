from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/<name>')
def get_name(name):
    return 'Hello {}!'.format(name)


@app.route('/data')
def names():
    data = {"Names": ["Anna", "Joanna", "Thomas", "CK", "John"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
