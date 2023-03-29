from flask import Flask, render_template
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

import os

app = Flask(__name__)
app.secret_key = os.environ["secret_key"]


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length(min=8)])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log in")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)