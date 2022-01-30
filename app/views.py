from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():
  """root page function that returns the index page and its data"""
  # get bbc news
  cnn_news_d = get_sources('terrorism')
  bbc_news_d = get_sources('business')
  title = 'News all over the world'

  return render_template('index.html', title=title, cnn = cnn_news_d, bbc= bbc_news_d )

@app.route('/art/<int:art_id>')
def art(art_id):
  """returns art details page and its data"""
  return render_template('art.html', id=art_id)