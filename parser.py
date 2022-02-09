import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/company/gms/blog/649227/'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.title.string)
find_replies = soup.find('div', class_='replies')
print(find_replies)