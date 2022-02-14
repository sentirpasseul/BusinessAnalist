import googlesearch
import urllib

import requests
from googlesearch import search
from search.input_search import input_search
from bs4 import BeautifulSoup

query = f"{input_search}"
query = query.replace(' ', '+')
url = "https://google.com/search?q="

req = requests.get(url+query)
h3 = req.find_all("h3",class_="r")
for elem in h3:
    elem=elem.contents[0]
    link=("https://www.google.com" + elem["href"])
    print(link)


#filtered = []
#for item in search(input_search, tld='co.in', num=10, stop=10, pause=2, lang='ru'):
    #filtered.append(item)
   # print(item)

#TODO Нужно сделать проверку на адрес вк, то есть проверку на url
#for item in filtered:
 #   filt1 = "" .join(filtered[item])
  #  print(filt1)