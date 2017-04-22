from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')


def index():
    return render_template("index.html")


@app.router('/users', methods = ["POST"])

def new_user():
    print request.form
    return redirect('/')





app.run(debug=True)
