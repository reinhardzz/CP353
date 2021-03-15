from flask import Flask,render_template,request,redirect
from models import db,Books
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top10food.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def index():
    all_book = Books.query.all()
    return render_template('index.html',data = all_book,title="Index")
    
if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)