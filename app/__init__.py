from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import url_for

app = Flask(__name__)

@app.route("/")
def intro():
    '''
    renders the corresponding html templates 
    with proper css and javascript links after using url_for instead of href
    '''
    return render_template("introduction.html")

@app.route("/introduction.html")
def introduction():
    '''
    renders the corresponding html templates 
    with proper css and javascript links after using url_for instead of href
    '''
    return render_template("introduction.html")

@app.route("/theory.html")
def theory():
    '''
    renders the corresponding html templates 
    with proper css and javascript links after using url_for instead of href
    '''
    return render_template("theory.html")

@app.route("/objective.html")
def objective():
    '''
    renders the corresponding html templates 
    with proper css and javascript links after using url_for instead of href
    '''
    return render_template("objective.html")
    
@app.route("/experiment.html")
def exp():
    '''
    renders the corresponding html templates 
    with proper css and javascript links after using url_for instead of href
    '''
    return render_template("experiment.html")

@app.route("/manual.html")
def manual():
    '''
    renders the corresponding html templates 
    with proper css and javascript links after using url_for instead of href
    '''
    return render_template("manual.html")

@app.route("/quizzes.html")
def quizzes():
    '''
    renders the corresponding html templates 
    with proper css and javascript links after using url_for instead of href
    '''
    return render_template("quizzes.html")

@app.route("/procedure.html")
def procedure():
    '''
    renders the corresponding html templates 
    with proper css and javascript links after using url_for instead of href
    '''
    return render_template("procedure.html")


@app.route("/refrences.html")
def ref():
    '''
    renders the corresponding html templates 
    with proper css and javascript links after using url_for instead of href
    '''
    return render_template("refrences.html")

@app.route("/feedback.html")
def feedback():
    '''
    renders the corresponding html templates 
    with proper css and javascript links after using url_for instead of href
    '''
    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)
