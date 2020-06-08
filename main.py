from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/badalportfolio'
db=SQLAlchemy(app)

""""	sno	fname	lname	email	msg	date	"""
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80),nullable=False)
    lname = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(20),  nullable=False)
    msg = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(120),  nullable=False)





@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact",methods=["GET","POST"])
def contact():


    return render_template("contact.html")
app.run(debug=True)
