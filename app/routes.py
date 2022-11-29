from flask import render_template
from app import app

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='index')

@app.route('/base')
def base():
    return render_template('base.html', title='base')