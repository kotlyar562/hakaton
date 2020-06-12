from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template("mainPage.html")

@app.route('/question1')
def question1():
    return render_template("question1.html")

@app.route('/question2')
def question2():
    return render_template("question2.html")

@app.route('/question3')
def question3():
    return render_template("question3.html")