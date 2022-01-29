from flask import render_template
from app import app

@app.route('/')
def index():
  """root page function that returns the index page and its data"""
  title = 'News all over the worl'
  return render_template('index.html', title=title)

@app.route('/art/<int:art_id>')
def art(art_id):
  """returns art details page and its data"""
  return render_template('art.html', id=art_id)