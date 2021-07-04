from . import app
from flask import render_template


@app.route('/')
def home():
    return render_template('layout.html')


@app.route('/test')
def test():
    return 'test'
