from app import app
import urllib.request, json
from .models import sources
from .models import allsources

Article = sources.Article
AllSources = allsources.AllSources

#GET API KEY
api_key = app.config['NEWS_API_KEY']

#GET NEWS BASE URL
base_url = app.config['NEWS_API_BASE_URL']

# ALL SOURCES URL
sources_url = app.config['SOURCES_API_URL']

def get_sources(newsources):
  """function that gets the json response of the url request"""
  get_sources_url = base_url.format(newsources,api_key)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    news_results = None

    if get_sources_response['articles']:
      sources_results_list = get_sources_response['articles']
      news_results = process_results(sources_results_list)

  return news_results

def process_results(news_list):
  """Function that processes news sources results and transform them to  a list of objects
  Args:
  news_list:list of dictionaries that contain news sources list

  Return:
  news_results: A list of newsources objects
  """

  news_results = []
  for news_item in news_list:
    id = news_item.get('id')
    description = news_item.get('description')
    url = news_item.get('url')
    title = news_item.get('title')
    urlToImage = news_item.get('urlToImage')

    if title and urlToImage and urlToImage!='null':
      news_object = Article(id,description,url,title,urlToImage)
      news_results.append(news_object)
      news_results = news_results[0:3]

  return news_results

def get_all_sources(sources):
  get_all_sources_url = sources_url.format(api_key)

  with urllib.request.urlopen(get_all_sources_url) as url:
    get_all_sources_data = url.read()
    get_all_sources_response = json.loads(get_all_sources_data)

    news_results = None

    if get_all_sources_response['sources']:
      all_sources_results_list = get_all_sources_response['sources']
      news_results = process_results_sources(all_sources_results_list)

  return news_results

def process_results_sources(sources_list):
    news_results = []
    
    for news_item in sources_list:
      id = news_item.get('id')
      name = news_item.get('name')

      if id:
        news_object =AllSources(id,name)
        news_results.append(news_object)
        news_results = news_results[0:10]

    return news_results

def get_article(id):
  get_article_details_url = base_url.format(id,api_key)

  with urllib.request.urlopen(get_article_details_url) as url:
    article_details_data = url.read()
    article_details_response = json.loads(article_details_data)

    # news_object = None
    # if article_details_response:
    #   id = article_details_response.get('id')
    #   description = article_details_response.get('description')
    #   url = article_details_response.get('url')
    #   title = article_details_response.get('title')
    #   urlToImage = article_details_response.get('urlToImage')


    #   news_object = Article(id,description,url,title,urlToImage)
      
  
  return process_results(article_details_response['articles'])