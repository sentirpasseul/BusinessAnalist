import math
import re
import string

split_regex = re.compile(r'[|!|?|…]')
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from nltk.tokenize import word_tokenize
import fasttext
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

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

def ton():
    print("ASS")


def preprocess_text(text1):
    text1 = " ".join(text1).lower().replace("ё", "е")
    text1 = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text1)
    text1 = re.sub('@[^\s]+', 'USER', text1)
    text1 = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text1)
    text1 = re.sub(' +', ' ', text1)
    text1 = re.sub('([0-9])', "\n", text1)
    return text1.strip()

def preprocess(text):

    ###РАЗДЕЛЕНИЕ ТЕКСТА НА ПРЕДЛОЖЕНИЯ
    #Удаление ненужных символов
    del_sym = preprocess_text(text).split("\n")
    print(del_sym)
    ##########################################


    znachenie_list = list()
    #Каждое предложение прогоняем по MorphAnalyzer
    for sentence in del_sym:
        #Сплитим предложение на слова
        sent1 = sentence.split(" ")
        list_parts = []

        print()
        #Разбиваем спличенный текст на токены
        sub1_reset = word_tokenize(" ".join(sent1))
        if sub1_reset != " " and sub1_reset !="":
            print(sub1_reset)

        # СЧЁТЧИК ВСЕХ СЛОВ В ТЕКСТЕ
        len_text = len(sub1_reset)
        print("Счётчик всех слов в тексте:", len_text, sep="\n")

        sum1 = 0
        #Анализируем каждое слово в предложении
        for word in sent1:
            if word != "":
                parse_parts = morph.parse(word)[0]
                part = parse_parts.tag.cyr_repr
                list_parts.append(part)
                print(f"Для слова '{word}' частью речи является '{part}'")

                #Сплитим строку из морф анализа
                morph_split = "".join(part).split(",")
                print(morph_split)

        form_xs = list()
        if len_text!=0:

            # ПЕРЕМЕННАЯ Х1 - КОЛИЧЕСТВО ЗАГЛАВНЫХ БУКВ

            for s in sentence:
                if s.isupper():
                   sum1 += 1
            count_uppercase = sum1
            # Вычисление эталона заглавных букв
            x1 = round(count_uppercase / len_text, 4)
            print(f"Переменная x1 (верхний регистр) = {round(x1, 4)}")
            form_xs.append(x1)

            # ПЕРЕМЕННАЯ Х2 - КОЛИЧЕСТВО СОЮЗОВ
            count_unions = list_parts.count("СОЮЗ")
            # Вычисление эталона союзов
            x2 = round(count_unions / len_text, 4)
            print(f"Переменная х2 (союзы) = {round(x2, 4)}")
            form_xs.append(x2)

            # ПЕРЕМЕННАЯ Х3 - КОЛИЧЕСТВО ЧАСТИЦ
            count_particle = list_parts.count("ЧАСТ")
            # Вычисление эталона частиц
            x3 = round(count_particle / len_text, 4)
            print(f"Переменная х3 (частицы) = {round(x3, 4)}")
            form_xs.append(x3)

            # ПЕРЕМЕННАЯ Х4 - КОЛИЧЕСТВО УСИЛИВАЮЩИХ ЗНАКОВ ПРЕПИНАНИЯ
            count_gain_punct = sub1_reset.count("!") + sub1_reset.count("?")
            # Вычисление эталона усиливающих знаков препинания
            x4 = round((count_gain_punct / len_text) / 10, 4)
            print(f"Переменная х4 = {x4}")
            form_xs.append(x4)

            # ПЕРЕМЕННАЯ Х5 - КОЛИЧЕСТВО МЕЖДОМЕТИЙ
            count_interj = list_parts.count("МЕЖД")
            # Вычисление эталона междометий
            x5 = round(count_interj / len_text, 4)
            print(f"Переменная х5 (междометия) = {x5}")
            form_xs.append(x5)

            max_x = max(form_xs)
            min_x = min(form_xs)
            formula = abs(math.sqrt(min_x**2 + max_x**2))
            znachenie_list.append(formula)

    print(znachenie_list)
    max_sarc_list = max(znachenie_list)
    min_sarc_list = min(znachenie_list)
    print("Максимальное значение сарказма:", max_sarc_list)
    print("Минимальное значение сарказма:", min_sarc_list)
    return znachenie_list, max_sarc_list, min_sarc_list

        #ТОКЕНИЗАЦИЯ
        #tokens = word_tokenize(" ".join(sentence))
        #print("ТОКЕНЫ: ", tokens)


def morph_analyzer():
    text = fifteen()
    preproc = preprocess(text)
# @classmethod

morph_analyzer()

