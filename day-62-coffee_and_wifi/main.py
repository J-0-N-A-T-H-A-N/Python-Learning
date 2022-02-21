from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location_url = StringField(label='Location URL', validators=[DataRequired(), URL()])
    open_time = StringField(label='Opening Time', validators=[DataRequired()])
    close_time = StringField(label='Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField(choices=["☕","☕☕","☕☕☕","☕☕☕☕","☕☕☕☕☕"], label='Coffee Rating', validators=[DataRequired()])
    wifi_rating = SelectField(choices=["✘","💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"],label='WiFi Rating', validators=[DataRequired()])
    power_rating = SelectField(choices = ["✘","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"], label='Power Outlets Rating', validators=[DataRequired()])
    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        new_cafe = [
            form.cafe.data,
            form.location_url.data,
            form.open_time.data,
            form.close_time.data,
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_rating.data
        ]
        entry = ",".join(new_cafe)
        with open('cafe-data.csv', "a", encoding="utf8") as csv_file:
            csv_file.write("\n" + entry)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)



if __name__ == '__main__':
    app.run(debug=True)
