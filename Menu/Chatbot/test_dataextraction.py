# Mitchell Martin
# 10/11/2022

import unittest
from dataextraction import *

class TestExtractions(unittest.TestCase):
   """Test the dataextractions from the dataextraction.py file"""
   
   def __init__(self, methodName: str = ...) -> None:
      super().__init__(methodName)
      self.error = not_connected()
   
   def test_check_stories(self):
      """Checks if the stories return."""
      self.assertNotEqual(get_stories(), self.error)
      self.assertIsInstance(get_stories(), str)
      
   def test_check_dates(self):
      """Checks if the dates are returned accurately."""
      self.assertNotEqual(get_date(), self.error)
      self.assertIsInstance(get_date(), str)
   
   def test_get_wait_times(self):
      """Checks if the wait times contain 'min'"""
      self.assertFalse(False, "min" in get_wait_times())
      
if __name__ == "__main__":
   unittest.main()
