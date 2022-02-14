import re
import string
import nltk
from nltk.tokenize import word_tokenize
from engine.preprocessing.preprocessing import sub1
import pymorphy2
morph = pymorphy2.MorphAnalyzer()


nltk.download("")

file = open(f'tests/100_sarc.txt', 'r', encoding='utf-8')
f = " ".join(file.read().splitlines())
print("\nПервоначальный текст: ", f, "\n", sep="\n")
"""
relist = re.sub("", f)
print(relist)
"""
list_file = f.split()
print("Текст добавлен в список: ",list_file, sep="\n")

#TODO сделать всё по функциям
""""
def counts(f):
    count_uppercase = f.count(f.ascii_uppercase)
    print(count_uppercase)
counts(f)
"""

#СЧЁТЧИК ВСЕХ СЛОВ В ТЕКСТЕ
len_text = len(list_file)
print("\nСчётчик всех слов в тексте:", len_text, sep="\n")

#ТОКЕНИЗАЦИЯ
tokens = word_tokenize(" ".join(list_file))
print("ТОКЕНЫ: ", tokens)

#ОПРЕДЕЛЕНИЕ ЧАСТЕЙ РЕЧИ
list_parts = []
sub1_reset = word_tokenize(sub1)
for word in sub1_reset:
    parse_parts = morph.parse(word)[0]
    part = parse_parts.tag.cyr_repr
    list_parts.append(part)
    print(f"Для слова '{word}' частью речи является '{part}'")

#РАЗБИВКА ПО СИМВОЛАМ
symbols_text = []
for word_i in range(len(f)):
    symbols_text.append(f[word_i])
len_symb_text = len(symbols_text)

#print(" ".join(symbols_text))

#ПЕРЕМЕННАЯ Х1 - КОЛИЧЕСТВО ЗАГЛАВНЫХ БУКВ
count_uppercase = sum(map(str.isupper, f))
#Вычисление эталона заглавных букв
x1 = (count_uppercase/len_symb_text)
print(f"Переменная x1 = {round(x1, 4)}")

#ПЕРЕМЕННАЯ Х2 - КОЛИЧЕСТВО СОЮЗОВ
count_unions = list_parts.count("СОЮЗ")
#Вычисление эталона союзов
x2 = (count_unions/len_text)
print(f"Переменная х2 = {round(x2, 4)}")


#ПЕРЕМЕННАЯ Х3 - КОЛИЧЕСТВО ЧАСТИЦ
count_particle = list_parts.count("ЧАСТ")
#Вычисление эталона частиц
x3 = count_particle/len_text
print(f"Переменная х3 = {round(x3, 4)}")

print("\nКоличество букв в верхнем регистре (переменная х1): ", count_uppercase)
print("Количество союзов в тексте:", count_unions)
print("Количество частиц в тексте:", count_particle)