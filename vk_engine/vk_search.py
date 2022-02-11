import json
import os.path

import requests
from auth_data import token
from collections import Counter

input_search = input("Введите название бизнеса:")
group_name = input_search

url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=10&access_token={token}&v=5.131"
req = requests.get(url)
print(req.text)

def get_wall_posts(group_name):
    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=10&access_token={token}&v=5.131"
    req = requests.get(url)
    src = req.json()

    #проверяем существует ли директория с именем группы
    if os.path.exists(f"{group_name}"):
        print(f"Директория с именем {group_name} уже существует!")
    else:
        os.mkdir(group_name)

    #сохраняем данные в json файл
    with open(f"{group_name}/{group_name}.json", "w", encoding="utf-8") as file:
        json.dump(src, file, indent=4, ensure_ascii=False)

    #собираем ID новых постов
    fresh_posts_id = []
    posts = src["response"]["items"]

    for fresh_post_id in posts:
        fresh_post_id = fresh_post_id["id"]
        fresh_posts_id.append(fresh_post_id)

    if not os.path.exists(f"{group_name}/exist_posts_{group_name}.txt"):
        print("Файла с ID постов не существует, создаём файл!")

        with open(f"{group_name}/exist_posts_{group_name}.txt", "w") as file:
            for item in fresh_posts_id:
                file.write(str(item)+"\n")

    else:
        print("Файл с ID постов найден, начинаем выборку постов")

    print(fresh_posts_id)
    get_comments_post(fresh_posts_id, posts)

    #ИЗВЛЕКАЕМ ДАННЫЕ ИЗ ПОСТОВ
    #count_comments = Counter(posts["comments"])
    #print(count_comments)
    #for post in posts:
     #   count_comments = Counter("co")

        #try:
         #   if "comments" in post:
        #except Exception:
            #print("Что-то пошло не так!")

def get_comments_post(fresh_posts_id, posts):
    print("GET COMMENTS POST")
    posts_id = []
    for item in fresh_posts_id:
        url = f"https://api.vk.com/method/wall.getComments?domain={item}&count=10&access_token={token}&v=5.131"
        req = requests.get(url)
        src = req.json()




def main():
    group_name = input_search
    get_wall_posts(group_name)


if __name__ == '__main__':
    main()