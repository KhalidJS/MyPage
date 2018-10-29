from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('Submit-button') == 'submit':
            text = request.form['username']
            password = request.form['password']
            print("submitted")
            print("A user with username:" + text + " and with password: ' " + password + " 'has looged in")
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
