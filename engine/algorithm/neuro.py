from engine.preprocessing.input_text import f
import re
import numpy as np
import pandas as pd
import sqlite3

# Считываем данные
n = ['id', 'date', 'name', 'text', 'typr', 'rep', 'rtw', 'faw', 'stcount', 'foll', 'frien', 'listcount']
data_positive = pd.read_csv('data/positive.csv', sep=';', error_bad_lines=False, names=n, usecols=['text'])
data_negative = pd.read_csv('data/negative.csv', sep=';', error_bad_lines=False, names=n, usecols=['text'])

# Формируем сбалансированный датасет
sample_size = min(data_positive.shape[0], data_negative.shape[0])
raw_data = np.concatenate((data_positive['text'].values[:sample_size],
                           data_negative['text'].values[:sample_size]), axis=0)
labels = [1] * sample_size + [0] * sample_size




"""""
data = [preprocess_text(t) for t in raw_data]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=1)

conn = sqlite3.connect('my')
"""

""""
async def read_file():
    timer = time.time()
    file = open(f'tests/100_sarc.txt', 'r', encoding='utf-8')
    f = " ".join(file.read().splitlines())
    print("\nПервоначальный текст: ", f, "\n", sep="\n")
    #relist = re.sub("", f)
    #print(relist)
    list_file = f.split()
    print("Текст добавлен в список: ",list_file, sep="\n")

    #TODO сделать всё по функциям
    def counts(f):
        count_uppercase = f.count(f.ascii_uppercase)
        print(count_uppercase)
    counts(f)





    for s in list_text:
        #ПЕРЕМЕННАЯ Х1 - КОЛИЧЕСТВО БУКВ В ВЕРХНЕМ РЕГИСТРЕ
        count_uppercase = sum(map(str.isupper, s))
        # ВЫЧИСЛЕНИЕ ЭТАЛОНА БУКВ В ВЕРХНЕМ РЕГИСТРЕ
        x1 = round(count_uppercase / len(s), 4)
        print(f"Переменная x1 = {round(x1, 4)}")

        # ПЕРЕМЕННАЯ Х2 - КОЛИЧЕСТВО СОЮЗОВ
        count_unions = list_text.count("СОЮЗ")
        # Вычисление эталона союзов
        x2 = round(count_unions / len_text, 4)
        print(f"Переменная х2 = {round(x2, 4)}")

        # ПЕРЕМЕННАЯ Х3 - КОЛИЧЕСТВО ЧАСТИЦ
        count_particle = list_parts.count("ЧАСТ")
        # Вычисление эталона частиц
        x3 = round(count_particle / len_text, 4)
        print(f"Переменная х3 = {round(x3, 4)}")

        # ПЕРЕМЕННАЯ Х4 - КОЛИЧЕСТВО УСИЛИВАЮЩИХ ЗНАКОВ ПРЕПИНАНИЯ
        count_gain_punct = f.count("!") + f.count("?")
        # Вычисление эталона усиливающих знаков препинания
        x4 = round((count_gain_punct / len_sent) / 10, 4)
        print(f"Переменная х4 = {x4}")

        # ПЕРЕМЕННАЯ Х5 - КОЛИЧЕСТВО МЕЖДОМЕТИЙ
        count_interj = list_parts.count("МЕЖД")
        # Вычисление эталона междометий
        x5 = round(count_interj / len_text, 4)
        print(f"Переменная х5 = {x5}")
        display_counts(count_uppercase, count_unions, count_particle, count_gain_punct, count_interj, timer)
        
"""""

