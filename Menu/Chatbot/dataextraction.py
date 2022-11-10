# Mitchell Martin
# 10/15/2022
# Tests for extracting data from shannon.
from multiprocessing.connection import wait
from bs4 import BeautifulSoup
import requests
import calendar
import datetime
import unittest
import time

try:
   page = requests.get('https://www.shannonhealth.com/')
   soup = BeautifulSoup(page.content, 'html.parser')
   title = soup.title.text

   page2 = requests.get('https://www.shannonhealth.com/contact-us/')
   soup2 = BeautifulSoup(page2.content, 'html.parser')

   # Extracting wait times
   wait_times_html = soup.find("div", class_="col-xs-12")
   wait_times = wait_times_html.find("ul")

   # Locating women & children hospital location.
   w_location = soup.find("div", class_="c-featured-location__text clearfix").find("p").text

   # Grabbing data from the health news.
   get_news = soup.find("div", class_="healthNews")
   get_news = get_news.find("ul")
   get_news = get_news.text

   # Grabbing data from the sleep center.
   page3 = requests.get('https://www.shannonhealth.com/services/sleep-center/')
   soup3 = BeautifulSoup(page3.content, 'html.parser')


   page4 = requests.get('https://www.shannonhealth.com')
   soup4 = BeautifulSoup(page4.content, 'html.parser')
   get_events = soup4.find("div", class_="classesEvents")

   # All the pages used for extracting
   # Shannon's data.
   pages = [ page, page2, page3, page4 ]
except:
   print("Exception: Could not connect to the internet.")

def get_stories():
   """Returns the latest stories."""
   try:
      s = get_events.text
      s += '\nMore information on https://www.shannonhealth.com/'
      return s
   except:
      return not_connected()

   
   
def get_shannon_info():
   try:
      s = "325.655.8191 | 324.481.2207 (fax)"
      s += '\nMonday through Friday'
      s += "\n8 a.m. to 6 p.m."
      return s
   except:
      return not_connected()

def get_date():
   """Returns the current date."""
   try:
      theday = "Today is " + str(calendar.day_name[datetime.date.today().weekday()])
      theday += ".\n Moreover, the current date is " + str(datetime.date.today()) + "."
      return theday
   except:
      return not_connected()

def not_connected():
   msg = "Waiting for an internet connection..."
   return msg

# Methods
def get_name():
   """Prints the hospital name."""
   try:
      return title[7:]
   except:
      return not_connected()

def get_wait_times():
   """Prints the wait times"""
   try:
      return wait_times.text
   except:
      return not_connected()

def get_women_location():
   """Prints the location"""
   try:
      return w_location
   except:
      return not_connected()

def return_news():
   """Returns latest news"""
   try:
      s = get_news.rstrip('\n')
      s += '\nMore information on https://www.shannonhealth.com/'
      return s
   except:
      return not_connected()

def news_item():
   try:
      everything = []
      test = ''
      i = 1
      pre = ''
      for line in return_news():
         if pre.find('\n') == -1:
            if line == '.' or (line.isupper() and pre.islower()):
               line += '\n'
               everything.append(test)
               test = ''
            test += line
         pre = line
      return everything
   except:
      return not_connected()

print(news_item())

if __name__ == '__main__':
   unittest.main()