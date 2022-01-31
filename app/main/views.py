from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_all_sources,get_article
from ..models import Article,AllSources

@main.route('/')
def index():
  """root page function that returns the index page and its data"""
  # get bbc news
  cnn_news_d = get_sources('terrorism')
  bbc_news_d = get_sources('business')
  sports = get_sources('sports')
  technology =get_sources('technology')
  politics = get_sources('politics')

  allsources = get_all_sources('')
  title = 'News all over the world'

  return render_template('index.html', title=title, terror = cnn_news_d, biz= bbc_news_d,sports=sports,technology=technology,politics=politics, sources=allsources)

@main.route('/source/<id>')
def source(id):
  """returns art details page and its data"""

  source = get_article(id)
  # title = f'{source.title}'
  return render_template('article.html', news=source)