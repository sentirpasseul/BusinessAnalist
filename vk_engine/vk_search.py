import requests
from auth_data import token

input_search = input("Введите название бизнеса:")
group_name = input_search

url = f"https://api.vk.com/method/groups.getByid?domain={group_name}&count=40&access_token={token}&v5.74"
req = requests.get(url)
print(req.text)