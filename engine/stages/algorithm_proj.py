import re
import string
import nltk

from engine.stages.stage1_sarcasm import text
import pymorphy2
import asyncio
import time
morph = pymorphy2.MorphAnalyzer()

nltk.download("")

def display_counts(count_uppercase,count_unions, count_particle, count_gain_punct, count_interj, timer ):
    print("\nКоличество букв в верхнем регистре (переменная х1): ", count_uppercase)
    print("Количество союзов в тексте:", count_unions)
    print("Количество частиц в тексте:", count_particle)
    print("Количество усиливающих знаков препинания в тексте:", count_gain_punct)
    print("Количество междометий в тексте:", count_interj)
    print(timer)
async def counters(len_symb_text, list_parts, len_text, f, len_sent, timer):
        # ПЕРЕМЕННАЯ Х1 - КОЛИЧЕСТВО ЗАГЛАВНЫХ БУКВ
        count_uppercase = sum(map(str.isupper, f))
        # Вычисление эталона заглавных букв
        x1 = round(count_uppercase / len_symb_text, 4)
        print(f"Переменная x1 = {round(x1, 4)}")

        # ПЕРЕМЕННАЯ Х2 - КОЛИЧЕСТВО СОЮЗОВ
        count_unions = list_parts.count("СОЮЗ")
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
        await asyncio.sleep(3)
        display_counts(count_uppercase,count_unions, count_particle, count_gain_punct, count_interj, timer )



""""
standard_100 = open(f'/standards/standard_100', 'w')
with open(f'/standards/standard_100', 'w'):
    display_counts(count_uppercase, count_unions,
                   count_particle, count_gain_punct,
                    count_interj)
"""

