from flask import render_template

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='index')