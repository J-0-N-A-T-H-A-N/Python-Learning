from flask import Flask, render_template, request

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact_form", methods=["POST"])
def receive_data():
    username = request.form['username']
    password = request.form['password']
    return (f"<h1>Name: {username} Password: {password}</h1>")


app.run(debug=True)