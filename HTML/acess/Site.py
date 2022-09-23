import random

from flask import Flask, render_template

app = Flask(__name__)


# rout

# função
@app.route("/")
def homepage():

    name=["jowjow","Bruno","Galera"]
    return render_template("index.html", **{"name":random.choice(name)})

@app.route("/bruno")
def homepag():

    name=["jowjow","Bruno","Galera"]
    return render_template("index.html", **{"name":"bruno"})


if __name__ == "__main__":
    app.run(debug=True)
