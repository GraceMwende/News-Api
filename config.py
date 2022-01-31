import os

class Config:
  """general configuration parent class"""
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
  SOURCES_API_URL= 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')

                      

class ProdConfig(Config):
  """production configuration child class
  Args:
    Config:The parent config class with General configuration settings
  """
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
  'development' :DevConfig,
  'production':ProdConfig
}