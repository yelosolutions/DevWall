from flask import render_template, url_for
from app import app

@app.route('/index')
def index():
    return render_template('index.html', title='index')

@app.route('/base')
def base():
    return render_template('base.html', title='base')

@app.route('/profile')
def profile():
    # code for rendering the user profile page
    return render_template('profile.html')

@app.route('/landing')
@app.route('/')
def landing():
    return render_template('landing.html', title='landing page')

@app.route('/login')
def login():
        return render_template('login.html', title='login')

@app.route('/signup')
def signup():
        return render_template('signup.html', title='signup')