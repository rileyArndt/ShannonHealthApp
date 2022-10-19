# Mitchell Martin
# 10/15/2022
# Tests for extracting data from shannon.
from multiprocessing.connection import wait
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.shannonhealth.com/')
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text

# Extracting wait times
wait_times_html = soup.find("div", class_="c-header-wait-times")
wait_times = wait_times_html.find("ul")

# Grabbing women & children hospital location
w_location = soup.find("div", class_="c-featured-location__text clearfix").find("p").text


# Methods
def get_name():
   """Prints the hospital name."""
   return title[7:]

def get_wait_times():
   """Prints the wait times"""
   wait_times = soup.find("span", class_="js-wait-north")
   return wait_times
def get_women_location():
   """Prints the location"""
   return w_location


