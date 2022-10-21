# Mitchell Martin
# 10/15/2022
# Tests for extracting data from shannon.
from multiprocessing.connection import wait
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.shannonhealth.com/')
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text

page2 = requests.get('https://www.shannonhealth.com/contact-us/')
soup2 = BeautifulSoup(page2.content, 'html.parser')

# Extracting wait times
wait_times_html = soup.find("div", class_="col-xs-12")
wait_times = wait_times_html.find("ul")

# Grabbing women & children hospital location
w_location = soup.find("div", class_="c-featured-location__text clearfix").find("p").text

get_news = soup.find("div", class_="healthNews")
# get_news = get_news.find("ul")
get_news = get_news.find("ul")

get_news = get_news.text

page3 = requests.get('https://www.shannonhealth.com/services/sleep-center/')
soup3 = BeautifulSoup(page3.content, 'html.parser')









# Methods
def get_name():
   """Prints the hospital name."""
   return title[7:]

def get_wait_times():
   """Prints the wait times"""
   wait_times
   return wait_times.text
def get_women_location():
   """Prints the location"""
   return w_location

def return_news():
   """Returns latest news"""
   return get_news.rstrip('\n')



