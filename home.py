import bcrypt
from dotenv import load_dotenv
import os
from flask import Flask, request, render_template,redirect,url_for
from forms import registration, loginForm
from pymongo import MongoClient
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c6bc198d0cf9298f7398bcdd45c2e13a'

session = {}

load_dotenv()
print(os.environ["MONGO_URI"]) #ask me for the mongo uri

client = MongoClient(os.environ["MONGO_URI"])
db = client.Quanta

print("lol")
print(db.users.find_one({"username":"lol"}))

@app.route('/')
@app.route('/login',methods=['post','get'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        return 'success'
    return render_template('login.html',title="login",form=form)


@app.route('/register',methods=['POST','GET'])
def register():
    form = registration()
    if request.method == 'POST' and form.validate_on_submit():
        existing_user = db.users.find_one({'email':form.email.data})

        if existing_user is None:
            hashpass = bcrypt.hashpw(form.password.data.encode('utf-8'),bcrypt.gensalt())
            db.users.insert_one({'username':form.username.data,'email':form.email.data,'password':hashpass})
            inserted_user = db.users.find_one({'username':form.username.data})
            session['email'] = form.email.data
            session['username'] = form.username.data
            session['id'] = inserted_user.get('_id')
            print(session)
            return redirect(url_for('payment'))
        else : return render_template('register.html',title="register",form=form,existing_check = True)
    
    else: return render_template('register.html',title="register",form=form)


@app.route('/payment',methods=['post','get','put'])
def payment():
    return render_template('payment.html')



def home():
    return render_template('home.html',name="lol")




if __name__ == "__main__":
    app.run(host='localhost',port=4444,debug=True)

