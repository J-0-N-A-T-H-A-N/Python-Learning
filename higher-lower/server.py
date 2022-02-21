from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img style="width: 450px" src="https://media0.giphy.com/media/l378khQxt68syiWJy/200w.webp?cid=' \
           'ecf05e4707th35arqw1vd4zvpiegjhp9mav61fb1qdx93m40&rid=200w.webp&ct=g">'


@app.route("/<int:guess>")
def guess_page(guess):
    if guess == rand_num:
        return '<h1>Correct!!</h1>' \
               '<img style="width: 450px" src="https://media2.giphy.com/media/ummeQH0c3jdm2o3Olp/200.webp?cid=' \
               'ecf05e47rk9vfci4u7tde0885t9s5sbaa71zoo7r18tpb6bm&rid=200.webp&ct=g">'
    elif guess < rand_num:
        return '<h1 style="color: blue">Nope! Too low!</h1>' \
               '<img style="width: 450px" src="https://media3.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/200w.webp?cid=' \
               'ecf05e47mu4w7lh9wms26elrayty9z191n90pby1enf5k8ps&rid=200w.webp&ct=g">'
    elif guess > rand_num:
        return '<h1 style="color: red">Nope! Too high!</h1>' \
               '<img style="width: 450px" src="https://media0.giphy.com/media/l46Cimsx66UsMWubK/200w.webp?cid=' \
               'ecf05e47qlca7kfn6ks9buovw3pey3ob4wkqs55t67c8shsx&rid=200w.webp&ct=g">'

rand_num = random.randint(0, 9)
print(rand_num)

if __name__ == "__main__":
    app.run(debug=True)


