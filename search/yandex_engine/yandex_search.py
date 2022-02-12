from search.input_search import input_search

import requests
import json
import os.path



""""
url = f'https://yandex.ru/search/?lr=198&clid=2270456&win=506&text={input_search}'
req = requests.get(url)

print(req.text)
def get_sites(fresh_sites_id):
    for site in fresh_sites_id:
        url = f"https://yandex.ru/search/?lr=198&clid=2270456&win=506&text={input_search}"
        req = requests.get(url)
        src = req.json()

        with open(f"{input_search}/{input_search}.json", "w", encoding="utf-8") as file:
            json.dump(src, file, indent=4, ensure_ascii=False)
"""

