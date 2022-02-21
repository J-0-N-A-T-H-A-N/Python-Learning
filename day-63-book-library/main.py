import sqlalchemy.sql.expression
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Silences SQLAlchemy deprecation warning

db = SQLAlchemy(app)
Bootstrap(app)


# Create the Book table using SQLAlchemy
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(50), unique=False, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


db.create_all()


class BookForm(FlaskForm):
    book_title = StringField(label="Title", validators=[DataRequired()])
    book_author = StringField(label="Author", validators=[DataRequired()])
    book_rating = SelectField(choices=range(0, 11), label="Rating", validators=[DataRequired()])
    submit = SubmitField(label='Add Book')


class EditForm(FlaskForm):
    book_rating = SelectField(choices=range(0, 11), label="Rating", validators=[DataRequired()])
    submit = SubmitField(label='Update')


class DeleteForm(FlaskForm):
    submit = SubmitField(label='Delete')


class SortForm(FlaskForm):
    sort_by = SelectField(choices=["Title", "Author", "Rating"], label="Sort by:", validators=[DataRequired()])
    submit = SubmitField(label='Sort')


@app.route('/', methods=["POST", "GET"])
def home():
    form = SortForm()
    all_books = Book.query.order_by(Book.title.asc()).all()
    if form.validate_on_submit():
        sort_field = form.sort_by.data.lower()
        if sort_field == "title":
            all_books = Book.query.order_by(Book.title.asc()).all()
        elif sort_field == "author":
            all_books = Book.query.order_by(Book.author.asc()).all()
        else:
            all_books = Book.query.order_by(Book.rating.desc()).all()

    return render_template('index.html', book_list=all_books, form=form)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        book_title = form.book_title.data.title()
        book_author = form.book_author.data.title()
        book_rating = int(form.book_rating.data)

        # Create the new book and add to the database (id is auto-generated)
        new_book = Book(title=book_title, author=book_author, rating=book_rating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/edit/<b_title>/<action>", methods=["POST", "GET"])
def edit(b_title, action):
    form = EditForm()
    book_to_edit = Book.query.filter_by(title=b_title).first()
    book_rating = book_to_edit.rating
    if action == "edit_book":
        if form.validate_on_submit():
            new_rating = int(form.book_rating.data)

            book_to_update = Book.query.filter_by(title=b_title).first()

            book_to_update.rating = new_rating
            db.session.commit()
            return redirect(url_for("home"))
        return render_template("edit.html", title=b_title, form=form, orig_rating=book_rating)
    elif action == "delete_book":
        form = DeleteForm()
        if form.validate_on_submit():
            book_to_update = Book.query.filter_by(title=b_title).first()
            db.session.delete(book_to_update)
            db.session.commit()
            return redirect(url_for("home"))
        return render_template("delete.html", title=b_title, form=form)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
