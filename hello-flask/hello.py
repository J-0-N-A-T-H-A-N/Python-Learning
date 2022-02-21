from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function


def make_italic(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function


@app.route("/")
def hello_world():
    return '<h1 style="color: red;text-align: center">Hello, World! How are you doing?</h1>' \
           '<p style="text-align: center">This is a bit of a blurb about me</p>' \
           '<img src="https://media.istockphoto.com/photos/gray-british-cat-kitten-picture-id1086004080?k=' \
           '20&m=1086004080&s=612x612&w=0&h=tvQKNjBGIsfCmUPR8YVJYfjLrTZ9JINbisKRjMj87IY=">'


@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye!"


@app.route("/<name>/<int:number>")                   # Variable Routing
def greet(name, number):
    return f"Hello, {name.capitalize()}, are you {number} years old?"


if __name__ == "__main__":
    app.run(debug=True)
