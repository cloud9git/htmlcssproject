from flask import Flask, render_template
app= Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/about")
def about():
    name="badal saini"
    return render_template("about.html",name=name)
@app.route("/boot")
def boot():
    return render_template("boot.html")
app.run(debug=True)
