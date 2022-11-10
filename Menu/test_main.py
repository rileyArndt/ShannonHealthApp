# Mitchell Martin
# 10/11/2022

# Testing the functionality of main

import unittest
from main import *
from Perscription import perscreen

class AppTest(unittest.TestCase):
   """Tests the app's functionality"""
   
   def test_app_build(self):
      """Checks if the MainApp is an instance of the App class."""
      self.assertNotEqual(MainApp.build, 0)
      
   def test_load_medication(self):
      """Checks if medication has been delivered to any pharmacy."""
      self.assertNotEqual(perscreen.PersLookScreen.get_records, [])
      self.assertNotEqual(perscreen.AllPersScreen.get_records, [])

if __name__ == '__main__':
   unittest.main()