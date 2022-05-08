import math
import re
from tonality import tonality
#from ui.main_ui import input_text
import nltk.downloader
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from collocations import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasttext
import pymorphy2
from gensim.models import Word2Vec

split_regex = re.compile(r'[|!|?|…]')
morph = pymorphy2.MorphAnalyzer()
nltk.downloader.Downloader('webtext')

class Algorythm():

    def __init__(self, text):
        self.col_if = "".join(collocations_if)
        self.col_bi = "".join(collocations_bi)
        self.col_no = "".join(collocations_no)
        self.text = text

        print("!"*50)
        if text.count("\n") > 1:
            print("Строчек больше 1")
            self.count_sentence = text.count("\n")
            self.split_text = text.split("\n")
        else:
            print("Строчек меньше двух")
            self.count_sentence = text.count(".")
            self.split_text = text.split(".")
        self.neg_list, self.pos_list, self.neu_list = tonality(self.split_text)
        print(self.split_text)


    def preprocess(self):
        text = self.text
        # vis = vizual_ton(split_text, neg_list, pos_list, neu_list)
        counter = 0
        znachenie_list = list()

    def analyzer(self):
        text = self.text
        #w2v_model = Word2Vec(min_count=10, window=2, negative=10, alpha=0.03, min_alpha=0.0007, sample=6e-5, sg=1)
        ##w2v_model.build_vocab(dict1)
        #w2v_model.train(dict1, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
        #w2v_model.init_sims(replace=True)

        #dict = {'Sentence': split_text, 'Негативно': neg_list, "Позитивно": pos_list, "Нейтрально": neu_list}

        #df = pd.DataFrame(dict)
        #print(df_width)

        count_if = 0
        sentences_ton = list()
        count_bi = 0
        count_zap_no = 0
        count_interj = 0
        for sentence in self.split_text:

            #print(w2v_model.wv.most_similar(positive=[f"{sentence}"]))
            if self.col_if in sentence:
                count_if +=1
                print("ЕСТь")
            if self.col_bi in sentence:
                count_bi +=1
            if self.col_no in sentence:
                count_zap_no +=1

            #print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!")
            #print(sentence)
            #print("!!!!!!!!!!!!!!!!!!!!!!!", end="")

            # Сплитим предложение на слова
            sent1 = sentence.split(" ")
            list_parts = []

            #print()
            # Разбиваем спличенный текст на токены
            sub1_reset = word_tokenize(" ".join(sent1))
            #if sub1_reset != " " and sub1_reset != "":
                #print(sub1_reset)

            # СЧЁТЧИК ВСЕХ СЛОВ В ТЕКСТЕ
            len_text = len(sub1_reset)
            #print("Счётчик всех слов в тексте:", len_text, sep="\n")

            sum1 = 0
            # Анализируем каждое слово в предложении
            for word in sent1:
                if word != "":
                    word = re.sub("[,@\'?\.$%_]", "", word)
                    parse_parts = morph.parse(word)[0]
                    part = parse_parts.tag.cyr_repr
                    list_parts.append(part)
                    print(f"Для слова '{word}' частью речи является '{part}'")

                    # Сплитим строку из морф анализа
                    morph_split = "".join(part).split(",")
                    #print(morph_split)
                count_interj += list_parts.count("МЕЖД")
            #self.count_bi = sentence.count("бы")
           # self.count_zap_no = sentence.count(', но')

            """
            neg_sent, pos_sent, neu_sent = tonality(sentence)
    
            sum_neg_sent = math.fsum(neg_sent)
            sum_pos_sent = math.fsum(pos_sent)
            sum_neu_sent = math.fsum(neu_sent)
    
            print()
            print("Отрицательно:", sum_neg_sent)
            print("Положительно:", sum_pos_sent)
            print("Нейтрально:", sum_neu_sent)
            print()
            """
            #print("Количество БЫ:", count_bi)
            #print("Количество ', но'", count_zap_no)

            """
            form_xs = list()
            if len_text != 0:
    
    
                # ПЕРЕМЕННАЯ Х4 - КОЛИЧЕСТВО УСИЛИВАЮЩИХ ЗНАКОВ ПРЕПИНАНИЯ
                count_gain_punct = sub1_reset.count("!") + sub1_reset.count("?")
                # Вычисление эталона усиливающих знаков препинания
                x4 = round((count_gain_punct / len_text) / 10, 4)
                print(f"Переменная х4 = {x4}")
                form_xs.append(x4)
    
                
    
                max_x, max_x_index = max(form_xs), form_xs.index(max(form_xs)) + 1
                min_x, min_x_index = min(form_xs), form_xs.index(min(form_xs)) + 1
                formula = abs(math.sqrt(min_x ** 2 + max_x ** 2))
                znachenie_list.append(formula)
    
            """
            #print()
            #print("АНАЛИЗ ТОНАЛЬНОСТИ ПРЕДЛОЖЕНИЯ:")
            #print("###############################")
            #print("Отрицательно:", neg_list[counter])
            #print("Положительно:", pos_list[counter])
            #print("Нейтрально:", neu_list[counter])
            #print("################################")
            #print()
            #counter += 1

            """
            print("ВЫЧИСЛЕНИЕ ТОЧЕК МАКСИМУМА И МИНИМУМА ВХОЖДЕНИЯ В САРКАЗМ")
            print("##########################")
            print(znachenie_list)
            max_sarc_list = max(znachenie_list)
            min_sarc_list = min(znachenie_list)
            print("Максимальное значение сарказма", "(x" + f"{max_x_index}" + "):", max_sarc_list, )
            print("Минимальное значение сарказма", "(x" + f"{min_x_index}" + "):", min_sarc_list)
            print("##########################")
            """
        for sentence in zip(self.split_text, self.neg_list, self.neu_list, self.pos_list):
            df1 = pd.DataFrame(columns=["sentences", "Негативно", "Позитивно", "Нейтрально"])
        df = pd.DataFrame(sentences_ton)
        df_width = df.style.set_properties(subset=['Sentence'], **{'width': '300px'})

        print("ТЕСТИРОВАНИЕ ФУНКЦИИ")
        print(df)

        sum_neg = math.fsum(self.neg_list)
        sum_neu = math.fsum(self.neu_list)
        sum_pos = math.fsum(self.pos_list)

        if sum_pos != 0 or sum_neu != 0 or sum_neg != 0:
            diff_neg = sum_neg / self.count_sentence
            diff_neu = sum_neu / self.count_sentence
            diff_pos = sum_pos / self.count_sentence

            print()
            print("Вычисление меры негатива на одно предложение:", diff_neg)
            print("Вычисление меры позитива на одно предложение:", diff_pos)
            print("Вычисление меры нейтральности на одно предложение:", diff_neu)
            print()

        print()
        print("#########################")
        print("ОБЩАЯ ОЦЕНКА ТОНАЛЬНОСТИ ТЕКСТА")
        print("Отрицательно:", sum_neg)
        print("Положительно:", sum_neu)
        print("Нейтрально:", sum_pos)



        print("СЧЁТЧИК ВСЕХ ПРЕДЛОЖЕНИЙ В ТЕКСТЕ")
        print(self.count_sentence)

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
        words = " ".join(self.split_text).split(" ")
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
        print("СЧЁТЧИК ЧАСТИЦ 'НЕ, ВОТ, ЕСЛИ, БЫ, НО'")
        print("#############################")
        print('Количество "Не" в предложенни:', words.count("не"))
        print('Количество "Вот" в предложенни:', words.count("вот"))
        print('Количество "Если" в предложенни:', words.count("если"))
        print('Количество ", eсли" в предложенни:', count_if)
        print('Количество "Бы" в предложении:', count_bi)
        print('Количество ", но" в предложении:', count_zap_no)
        print("#############################")
        print()

        print("ВЫЧИСЛЕНИЕ ПО ФОРМУЛЕ")

        # ПЕРЕМЕННАЯ Х1 - КОЛИЧЕСТВО МЕЖДОМЕТИЙ

        # Вычисление эталона междометий
        x5 = count_interj
        print(f"Переменная х5 (междометия) = {x5}")



        print("!"*50)
        print()
        print()
        print()
    #print("Count Quotes:", count_q)





