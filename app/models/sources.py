class Sources:
  """sources object to define news sources"""
  def __init__(self,id,description,url,title,urlToImage):
    self.id = id
    # self.name = name
    self.description = description
    self.url = url
    self.title = title
    self.urlToImage = urlToImage
