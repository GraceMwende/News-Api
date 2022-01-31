import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
  """Test class to define the behavaiour of the articles class"""

  def setUp(self):
    """setup method that runs before every Test"""
    self.new_article = Article("bbc-news", "The move is with", "https://uytt", "Justice depart", "https://kjhg.jpg", "2022-01-11T23:02:06Z")

  def test_instance(self):
    self.assertTrue(self.new_article, Article)

