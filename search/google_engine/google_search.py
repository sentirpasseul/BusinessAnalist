import googlesearch
import urllib
import sys, webbrowser
import requests
from googlesearch import search
from search.input_search import input_search
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import time

url = f'https://www.google.ru/search?q={input_search}'
req = requests.get(url, headers={'User-agent': 'your bot 0.1'})
"""
url = f"https://www.google.ru/search?q={input_search}"
get_source(url)

#filtered = []
#for item in search(input_search, tld='co.in', num=10, stop=10, pause=2, lang='ru'):
    #filtered.append(item)
   # print(item)

#TODO Нужно сделать проверку на адрес вк, то есть проверку на url
#for item in filtered:
 #   filt1 = "" .join(filtered[item])
  #  print(filt1)
  """