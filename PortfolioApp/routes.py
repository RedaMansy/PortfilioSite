from PortfolioApp import app
from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    guy = "man"
    return render_template('index.html', guy=guy)

def about():
    return "About"
