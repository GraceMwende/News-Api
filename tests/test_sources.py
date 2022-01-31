import unittest
from app.models import AllSources

class SourcesTest(unittest.TestCase):
  """Test class to test the behaviour of the sources class"""
  
  def setUp(self):
    """setup method that runs before every Test"""

    self.new_source = AllSources("bbc-news", "BBC-news")

  def  test_instance(self):
    self.assertTrue(self.new_source, AllSources)