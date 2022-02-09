import vk

def get_members(groupid):  # Функция формирования базы участников сообщества в виде списка
  pass


def save_data(data, filename="data.txt"):  # Функция сохранения базы в txt файле
  pass


def enter_data(filename="data.txt"):  # Функция ввода базы из txt файла
  pass


def get_intersection(group1, group2):  # Функция нахождения пересечений двух баз
  pass


def union_members(group1, group2):  # Функция объединения двух баз без повторов
  pass


if __name__ == "__main__":
    token = ""  # Сервисный ключ доступа
    session = vk.Session(access_token=token)  # Авторизация
    vk_api = vk.API(session)