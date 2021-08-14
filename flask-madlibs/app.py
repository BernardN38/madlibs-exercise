from flask import Flask,request, render_template
from stories import story,Story
app = Flask(__name__)


@app.route('/')
def make_story():
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/display-story')
def display_story():
    responses = request.args
    return story.generate(responses)