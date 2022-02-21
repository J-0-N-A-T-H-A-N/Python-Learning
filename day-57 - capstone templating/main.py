from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

API_URL = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(API_URL)
posts = blog_response.json()
all_posts = []
for post in posts:
    new_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    all_posts.append(new_post)
print(all_posts)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:ref>')
def get_post(ref):
    return render_template("post.html", posts=all_posts, post_ref=ref)


if __name__ == "__main__":
    app.run(debug=True)
