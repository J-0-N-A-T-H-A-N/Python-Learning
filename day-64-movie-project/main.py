from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired
import requests
import random

class NewMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    review = TextAreaField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")

class UpdateForm(FlaskForm):
    rating = FloatField(label='Rating out of 10', validators=[DataRequired()])
    review = TextAreaField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie_database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Silences SQLAlchemy deprecation warning

db = SQLAlchemy(app)
Bootstrap(app)

# Create the Book table using SQLAlchemy
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(220), nullable=False, unique=True)
    rating = db.Column(db.Float, nullable=False)
    # ranking = db.Column(db.Float, nullable=False)       # Not used
    review = db.Column(db.String(80), nullable=False, unique=True)
    img_url = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return '<Book %r>' % self.title


db.create_all()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating.desc()).limit(10).all()
    num_movies = len(movies) + 1
    movies=movies[::-1]
    return render_template("index.html", movie_list=movies, num=num_movies)


@app.route("/add", methods=["POST", "GET"])
def add():
    add_movie = NewMovieForm()
    if add_movie.validate_on_submit():
        movie_title = add_movie.title.data.title()
        movie_review = add_movie.review.data

        tmdb_endpoint = "https://api.themoviedb.org/3/search/movie?"
        tmdb_api_key = "c90296a95e77d35018f8f9575f2805e4"
        params = {
            "api_key" : tmdb_api_key,
            "query" : movie_title
        }

        response = requests.get(tmdb_endpoint, params=params)
        response.raise_for_status()
        results = response.json()


        # random_rank = random.randint(0, 9999)

        new_movie = Movie(
            title=results["results"][0]["original_title"],
            year=int(results["results"][0]["release_date"].split("-")[0]),
            description=results["results"][0]["overview"],
            rating=results["results"][0]["vote_average"],
            review=movie_review,
            img_url=f"https://image.tmdb.org/t/p/w500/{results['results'][0]['poster_path']}",
            # ranking=random_rank
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html", form=add_movie)

@app.route("/edit/<m_id>/<action>", methods=["POST", "GET"])
def edit(m_id, action):
    edit_movie = UpdateForm()
    if action == "edit":
        if edit_movie.validate_on_submit():
            movie_to_edit = Movie.query.filter_by(id=m_id).first()
            new_rating = edit_movie.rating.data
            new_review = edit_movie.review.data
            movie_to_edit.rating = new_rating
            movie_to_edit.review = new_review
            db.session.commit()
            return redirect(url_for("home"))

    elif action == "delete":
        print("Deleting...")
        movie_to_delete = Movie.query.filter_by(id=m_id).first()
        db.session.delete(movie_to_delete)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", form=edit_movie)

if __name__ == '__main__':
    app.run(debug=True)
