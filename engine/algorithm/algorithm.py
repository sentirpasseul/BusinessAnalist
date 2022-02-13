import re
import string
import nltk
from nltk.tokenize import word_tokenize
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

#TODO СЧЁТЧИК ЗАГЛАВНЫХ БУКВ
""""
def counts(f):
    count_uppercase = f.count(f.ascii_uppercase)
    print(count_uppercase)
counts(f)
"""

#СЧЁТЧИК ВСЕХ СЛОВ В ТЕКСТЕ
len_text = len(list_file)
print("\nСчётчик всех слов в тексте:", len_text, sep="\n")

#ТОКЕНИЗАЦИЯ И РАЗБИВКА НА СИМВОЛЫ
tokens = word_tokenize(" ".join(list_file))
print("ТОКЕНЫ: ", tokens)

symbols_text = []
for word_i in range(len(f)):
    symbols_text.append(f[word_i])

print(" ".join(symbols_text))
#ПЕРЕМЕННАЯ Х1 - КОЛИЧЕСТВО ЗАГЛАВНЫХ БУКВ
count_uppercase = sum(map(str.isupper, f))
print("Количество слов в верхнем регистре (х1): ", count_uppercase)

#

