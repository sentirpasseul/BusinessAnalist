import math
import re
import string
from get_text import *
from tonality import *
import nltk.downloader
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import fasttext
import pymorphy2

split_regex = re.compile(r'[|!|?|…]')
morph = pymorphy2.MorphAnalyzer()
nltk.downloader.Downloader('webtext')

def preprocess_big_text():
    count_sentence = dataset_sarcasm.count("\n")
    split_text = dataset_sarcasm.split(".")
    print(split_text)

    neg_list, pos_list, neu_list = tonality(split_text)
    counter = 0

    znachenie_list = list()

    for sentence in split_text:

        print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!")
        print(sentence)
        print("!!!!!!!!!!!!!!!!!!!!!!!", end="")

        # Сплитим предложение на слова
        sent1 = sentence.split(" ")
        list_parts = []

        print()
        # Разбиваем спличенный текст на токены
        sub1_reset = word_tokenize(" ".join(sent1))
        if sub1_reset != " " and sub1_reset != "":
            print(sub1_reset)

        # СЧЁТЧИК ВСЕХ СЛОВ В ТЕКСТЕ
        len_text = len(sub1_reset)
        print("Счётчик всех слов в тексте:", len_text, sep="\n")

        sum1 = 0
        # Анализируем каждое слово в предложении
        for word in sent1:
            if word != "":
                parse_parts = morph.parse(word)[0]
                part = parse_parts.tag.cyr_repr
                list_parts.append(part)
                print(f"Для слова '{word}' частью речи является '{part}'")

                # Сплитим строку из морф анализа
                morph_split = "".join(part).split(",")
                print(morph_split)

        count_bi = sentence.count("бы")
        count_zap_no = sentence.count(','+'но')

        neg_sent, pos_sent, neu_sent = tonality(sentence)

        sum_neg_sent = math.fsum(neg_sent)
        sum_pos_sent = math.fsum(pos_sent)
        sum_neu_sent = math.fsum(neu_sent)

        print()
        print("Отрицательно:", sum_neg_sent)
        print("Положительно:", sum_pos_sent)
        print("Нейтрально:", sum_neu_sent)
        print()

        print("Количество БЫ:", count_bi)
        print("Количество ', но'", count_zap_no)


        form_xs = list()
        if len_text != 0:

            # ПЕРЕМЕННАЯ Х1 - КОЛИЧЕСТВО "БЫ"
            for s in sentence:
                if s.isupper():
                    sum1 += 1
            count_uppercase = sum1
            # Вычисление эталона "бы"
            x1 = count_bi
            print(f"\nПеременная x1 ('БЫ') = {round(x1, 4)}")
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

            max_x, max_x_index = max(form_xs), form_xs.index(max(form_xs)) + 1
            min_x, min_x_index = min(form_xs), form_xs.index(min(form_xs)) + 1
            formula = abs(math.sqrt(min_x ** 2 + max_x ** 2))
            znachenie_list.append(formula)


        print()
        print("АНАЛИЗ ТОНАЛЬНОСТИ ПРЕДЛОЖЕНИЯ:")
        print("###############################")
        print("Отрицательно:", neg_list[counter])
        print("Положительно:", pos_list[counter])
        print("Нейтрально:", neu_list[counter])
        print("################################")
        print()
        counter += 1

        print("ВЫЧИСЛЕНИЕ ТОЧЕК МАКСИМУМА И МИНИМУМА ВХОЖДЕНИЯ В САРКАЗМ")
        print("##########################")
        print(znachenie_list)
        max_sarc_list = max(znachenie_list)
        min_sarc_list = min(znachenie_list)
        print("Максимальное значение сарказма", "(x" + f"{max_x_index}" + "):", max_sarc_list, )
        print("Минимальное значение сарказма", "(x" + f"{min_x_index}" + "):", min_sarc_list)
        print("##########################")


    sum_neg = math.fsum(neg_list)
    sum_neu = math.fsum(neu_list)
    sum_pos = math.fsum(pos_list)

    print()
    print("#########################")
    print("ОБЩАЯ ОЦЕНКА ТОНАЛЬНОСТИ ТЕКСТА")
    print("Отрицательно:", sum_neg)
    print("Положительно:", sum_neu)
    print("Нейтрально:", sum_pos)

    print("СЧЁТЧИК ВСЕХ ПРЕДЛОЖЕНИЙ В ТЕКСТЕ")
    print(count_sentence)

        # Часто встречающиеся слова

    # Частота "не" в предложении

    #from nltk.corpus import stopwords
    #ru_stopwords = stopwords.words('russian')
    # tokens = word_tokenize(sentence, language='russian')
    filtered_tokens = []
    #for sentence in split_text:
        #for token in sentence:
            #if token not in ru_stopwords:
            #    filtered_tokens.append(token)
    words = " ".join(split_text).split(" ")
    count_q = words.count('"')
    if count_q > 0:
        count_q = True

    for word in words:
        filtered_tokens.append(word)

    fdist = FreqDist(filtered_tokens)
    print()
    print("ЧАСТОТА СЛОВ")
    print("########################")
    #print(*fdist.most_common(len(filtered_tokens)), sep='\n')
    print("########################")
    print()
    #fdist.plot(15)

    print()
    print("СЧЁТЧИК ЧАСТИЦ 'НЕ, ВОТ, ЕСЛИ'")
    print("#############################")
    print('Количество "Не" в предложенни:', words.count("не"))
    print('Количество "Вот" в предложенни:', words.count("вот"))
    print('Количество "Если" в предложенни:', words.count("если"))
    print("#############################")
    print()

    print("Count Quotes:", count_q)