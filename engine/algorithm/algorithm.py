import re
import string

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

