from flask import Flask

app = Flask(__name__)


# how to reader Html using flask
# getting old of what the user typed in the url

@app.route('/username')
def hello():
    return 'Hello'


@app.route('/username/<name>')
def greet(name):
    return f'Hello, {name}!'


# string-(default) accepts any text without a slash
@app.route('/username/<path:subpath>')
def show_subpath(subpath):
    return f'subpath, {subpath}'


# integer
@app.route('/username/<name>/<int:employee_id>')
def findById(name, employee_id):
    return f'Name: {name},  Employee_id:  {employee_id}'


# Flask can also render Html elements
@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, world!</h1>'


# using python decorators
def make_bold(function):
    def wrapper():
        return f'<strong>{function()}</strong>'

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'

    return wrapper


def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'

    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
