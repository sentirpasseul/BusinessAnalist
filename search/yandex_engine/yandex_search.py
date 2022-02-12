from search.input_search import input_search
import requests

url = f'https://yandex.ru/search/?lr=198&clid=2270456&win=506&text={input_search}'
req = requests.get(url)

print(req)