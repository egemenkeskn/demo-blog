from flask import Flask,request
from flask import render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    password = db.Column(db.String(30),unique=False,nullable=False)
    mail = db.Column(db.String(50),unique=True,nullable=False)
     id = db.Column(db.Integer,primary_key=True)
    password = db.Column(db.String(30),unique=False,nullable=False)
    mail = db.Column(db.String(50),unique=True,nullable=False)
     id = db.Column(db.Integer,primary_key=True)
    password = db.Column(db.String(30),unique=False,nullable=False)
    mail = db.Column(db.String(50),unique=True,nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        mail = request.form['email']
        password = request.form['password']
        new_user = user(password=password,mail=mail)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('signup_success'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)