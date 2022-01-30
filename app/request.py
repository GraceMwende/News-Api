from app import app
import urllib.request, json
from .models import sources

Sources = sources.Sources

#GET API KEY
api_key = app.config['NEWS_API_KEY']

#GET NEWS BASE URL
base_url = app.config['NEWS_API_BASE_URL']

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

    if title and urlToImage:
      news_object = Sources(id,description,url,title,urlToImage)
      news_results.append(news_object)

  return news_results

