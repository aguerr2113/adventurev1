from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from adventure import adventure_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    
    choices = adventure_story.choices

    return render_template('form.html', choices = choices)

@app.route('/result')
def choice():
    
    choices = request.args.get("choices")
    outcomes = adventure_story.generate(choices)

    return render_template('result.html', outcomes = outcomes)
