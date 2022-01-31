class AllSources:
  """sources object to define news sources"""
  def __init__(self,id,name):
    self.id = id
    self.name = name

class Article:
  """sources object to define news articles"""
  def __init__(self,id,description,url,title,urlToImage,publishedAt):
    self.id = id
    self.description = description
    self.url = url
    self.title = title
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
