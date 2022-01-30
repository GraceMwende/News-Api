class Config:
  """general configuration parent class"""
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
                      

class ProdConfig(Config):
  """production configuration child class
  Args:
    Config:The parent config class with General configuration settings
  """
  pass

class DevConfig(Config):
  DEBUG = True