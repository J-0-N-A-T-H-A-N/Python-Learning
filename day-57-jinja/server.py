from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)


@app.route("/")
def home():
    current_year = dt.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    AGIFY_URL = f"https://api.agify.io/?name={name}"
    GENDER_URL = f"https://api.genderize.io/?name={name}"
    agify_response = requests.get(AGIFY_URL).json()
    age = agify_response["age"]
    gender_response = requests.get(GENDER_URL).json()
    gender = gender_response["gender"]
    return render_template("guess.html", name=name.capitalize(), your_age=age, your_gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    BLOG_URL ="https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(BLOG_URL)
    blog_data = blog_response.json()
    return render_template("blog.html", all_posts=blog_data, number=num)

if __name__ == "__main__":
    app.run(debug=True)
