from flask import render_template
from app import app
from .request import get_sources,get_article

@app.route('/')
def index():
  """root page function that returns the index page and its data"""
  # get bbc news
  cnn_news_d = get_sources('terrorism')
  bbc_news_d = get_sources('business')
  sports = get_sources('sports')
  technology =get_sources('technology')
  politics = get_sources('politics')
  title = 'News all over the world'

  return render_template('index.html', title=title, terror = cnn_news_d, biz= bbc_news_d,sports=sports,technology=technology,politics=politics)

@app.route('/news/<int:id>')
def article(id):
  """returns art details page and its data"""

  article = get_article(id)
  title = f'{article.title}'
  return render_template('article.html', news=article)