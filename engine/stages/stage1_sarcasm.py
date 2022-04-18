import random
import re
split_regex = re.compile(r'[|!|?|…]')
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel, FastTextToxicModel
from engine.algorithm.algorithm import preprocess
import fasttext
import pandas as pd
import numpy as np
import sklearn
import pymorphy2
morph = pymorphy2.MorphAnalyzer

fasttext.FastText.eprint = lambda x: None
FastTextSocialNetworkModel.MODEL_PATH = 'fasttext-social-network-model.bin'

file = open(f'data.txt', 'r', encoding="utf-8")
text = file.read()
#only_text = re.sub(r'[\d]', '', text)

#class check_sarc():

# @staticmethod
def Question( s):
    for symbol in s:
        if "?" in symbol:
            d = True

#@staticmethod
def fifteen():
    #sentences = filter(lambda t: t, [t.strip() for t in text.split(r'[\d]')])
    #sentences = [s.strip() for s in split_regex.split(text)]
    sarc_sentences = []
    #rand_15 = random.randint()
    #15% из всего текста:
    #for
    list_text = (text.split('\n'))

    form_15 = (170*15)//100
    print(form_15)
    ar_15 = []
    for s in range(form_15):     # s - каждый текст от 1 до 25
        ar_15.append(list_text[s])

    return ar_15

def morph_analyzer():
    text = fifteen()
    preproces = preprocess(text)
    print(preproces)




# @classmethod
def ton():
    ar_15 = fifteen()

    tokenizer = RegexTokenizer()

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    # Распознавание тональности текста
    results = model.predict(ar_15, k=4)
    res_ton = dict
    for message, sentiment in zip(ar_15, results):
        neu = sentiment.get('neutral')
        p = sentiment.get('positive')
        neg = sentiment.get('negative')

        """
        print(message, '\n',
              'neutral = ', sentiment.get('neutral'), '\n',
              'positive = ', sentiment.get('positive'), '\n'
              'negative = ', sentiment.get('negative'), '\n'
              'negative = ', sentiment.get('negative'), '\n'
              'negative = ', sentiment.get('negative'))
        """
        return neu, p, neg

#@classmethod
def parts_speech():
    list_text = (text.split('\n'))
    print(list_text)



    """""
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
        """

#@classmethod
def math_model():
    tonality = ton()



#math_model()
#print(parts_speech())
morph_analyzer()