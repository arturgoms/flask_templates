__author__ = ["Marcelo Marcon", "github.com/mmarconm"]

#!/usr/bin/python3

# Importing Flask App
from flask import Flask
from flask import render_template

#Creating Decorator to call index page
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
