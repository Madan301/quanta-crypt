from dotenv import load_dotenv
import os
from flask import Flask, request, render_template
from forms import registration, loginForm
from pymongo import MongoClient
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c6bc198d0cf9298f7398bcdd45c2e13a'

load_dotenv()
print(os.environ["MONGO_URI"]) #ask me for the mongo uri

client = MongoClient(os.environ["MONGO_URI"])
db = client.Quanta

@app.route('/payment',methods=['post','get','put'])
def test():
    return render_template('hello.html')

@app.route('/register',methods=['post','get'])
def register():
    form = registration()
    if form.validate_on_submit():
        return 'success'
    return render_template('register.html',title="register",form=form)

@app.route('/login',methods=['post','get'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        return 'success'
    return render_template('login.html',title="login",form=form)


if __name__ == "__main__":
    app.run(host='localhost',port=4444,debug=True)

