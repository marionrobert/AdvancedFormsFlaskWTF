from flask import Flask, render_template
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField
import os

app = Flask(__name__)
app.secret_key = os.environ["secret_key"]


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)