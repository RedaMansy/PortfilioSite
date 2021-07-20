from PortfolioApp import app

@app.route('/')
@app.route('/home')
def home():
    return "test"
