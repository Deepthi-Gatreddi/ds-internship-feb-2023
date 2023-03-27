from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import string
import random
import validators
import os
from flask_migrate import Migrate


app = Flask(__name__)
basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,"data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

class Url(db.Model):
    __tablename__ ="Urls"
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_url = db.Column(db.String(10), unique=True)
    full_url = db.Column(db.String(500))

    def __init__(self, original_url, short_url,full_url):
        self.original_url = original_url
        self.short_url = short_url
        self.full_url = full_url

@app.before_first_request
def create_tables():
    db.create_all()

def shorten_url():
    chars = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(chars) for _ in range(6))
        full_url = request.host_url + short_url
        if not Url.query.filter_by(short_url=short_url).first():
            return short_url,full_url

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        if not validators.url(original_url):
            return render_template('error.html', message='Invalid URL')
        short_url, full_url = shorten_url()
        new_url = Url(original_url=original_url, short_url=short_url, full_url=full_url)
        db.session.add(new_url)
        db.session.commit()
        print(short_url)
        return render_template('result.html', short_url=full_url,original_url=original_url)
    return render_template('home.html')

@app.route('/<short_url>')
def redirect_to_original_url(short_url):
    url = Url.query.filter_by(short_url=short_url).first()
    return redirect(url.original_url)

@app.route('/history')
def history():
    urls = Url.query.all()
    return render_template('history.html', urls=urls)


if __name__ == "__main__":
    app.run(debug=True)