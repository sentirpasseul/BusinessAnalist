import math
import re
import string

import nltk.downloader

split_regex = re.compile(r'[|!|?|…]')
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import fasttext
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
nltk.downloader.Downloader('webtext')

fasttext.FastText.eprint = lambda x: None
FastTextSocialNetworkModel.MODEL_PATH = 'fasttext-social-network-model.bin'

file = open(f'data.txt', 'r', encoding="utf-8")
text = file.read()

file_big_text = open(f'test.txt', 'r', encoding='utf-8')
big_text = file_big_text.read()
#only_text = re.sub(r'[\d]', '', text)

#class check_sarc():

# @staticmethod
def Question( s):
    for symbol in s:
        if "?" in symbol:
            d = True

#@staticmethod

def split_big_text():
    list_text = (big_text.split('.'))
    return list_text

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


def preprocess_text(text1):
    text1 = " ".join(text1).lower().replace("ё", "е")
    text1 = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text1)
    text1 = re.sub('@[^\s]+', 'USER', text1)
    text1 = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text1)
    text1 = re.sub(' +', ' ', text1)
    text1 = re.sub('([0-9])', "\n", text1)
    return text1.strip()

def tonality(del_sym):
    fasttext.FastText.eprint = lambda x: None
    FastTextSocialNetworkModel.MODEL_PATH = 'fasttext-social-network-model.bin'

    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    results = model.predict(del_sym, k=4)
    neu_list = list()
    neg_list = list()
    pos_list = list()
    for sentence, sentiment in zip(del_sym, results):
        # Анализ Тональности предложения
        neu = sentiment.get('neutral')
        neu_list.append(neu)
        p = sentiment.get('positive')
        pos_list.append(p)
        neg = sentiment.get('negative')
        neg_list.append(neg)

        #print(sentence, '\n',
         #     'neutral = ', sentiment.get('neutral'), '\n',
          #    'positive = ', sentiment.get('positive'), '\n'
           #   'negative = ', sentiment.get('negative'), '\n'
            #  )
    for s in range(len(neg_list)):
        if neg_list[s] is None:
            neg_list[s] = 0
    for s in range(len(neu_list)):
        if neu_list[s] is None:
            neu_list[s] = 0
    for s in range(len(pos_list)):
        if pos_list[s] is None:
            pos_list[s] = 0
    return neg_list,neu_list,pos_list



def preprocess(text):

    ###РАЗДЕЛЕНИЕ ТЕКСТА НА ПРЕДЛОЖЕНИЯ
    #Удаление ненужных символов
    del_sym = preprocess_text(text).split("\n")
    print(del_sym)
    ##########################################

    neg_list, pos_list, neu_list = tonality(del_sym)
    counter = 0

    znachenie_list = list()
    #Каждое предложение прогоняем по MorphAnalyzer
    for sentence in del_sym:

        print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!")
        print(sentence)
        print("!!!!!!!!!!!!!!!!!!!!!!!", end="")

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
        no = 0
        vot = 0
        esli = 0
        for word in list_parts:
            if word == "не":
              no +=1
            else:
                if word == "вот":
                    vot +=1
                elif word == "если":
                    esli +=1

        form_xs = list()
        if len_text!=0:

            # ПЕРЕМЕННАЯ Х1 - КОЛИЧЕСТВО ЗАГЛАВНЫХ БУКВ
            for s in sentence:
                if s.isupper():
                   sum1 += 1
            count_uppercase = sum1
            # Вычисление эталона заглавных букв
            x1 = round(count_uppercase / len_text, 4)
            print(f"\nПеременная x1 (верхний регистр) = {round(x1, 4)}")
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




            max_x, max_x_index = max(form_xs), form_xs.index(max(form_xs))+1
            min_x, min_x_index = min(form_xs), form_xs.index(min(form_xs))+1
            formula = abs(math.sqrt(min_x**2 + max_x**2))
            znachenie_list.append(formula)

        print()
        print("СЧЁТЧИК ЧАСТИЦ 'НЕ, ВОТ, ЕСЛИ'")
        print("#############################")
        print('Количество "Не" в предложенни:', no)
        print('Количество "Вот" в предложенни:', vot)
        print('Количество "Если" в предложенни:', esli)
        print("#############################")
        print()

        #Часто встречающиеся слова
        from nltk.corpus import stopwords
        ru_stopwords = stopwords.words('russian')
        #tokens = word_tokenize(sentence, language='russian')
        filtered_tokens = []
        for token in sub1_reset:
            if token not in ru_stopwords:
                filtered_tokens.append(token)
        fdist = FreqDist(filtered_tokens)
        print()
        print("ЧАСТОТА СЛОВ")
        print("########################")
        print(*fdist.most_common(len(filtered_tokens)), sep='\n')
        print("########################")
        print()



        #Частота "не" в предложении
        f_ne = FreqDist(filtered_tokens)

        print()
        print("АНАЛИЗ ТОНАЛЬНОСТИ ПРЕДЛОЖЕНИЯ:")
        print("###############################")
        print("Отрицательно:", neg_list[counter])
        print("Положительно:", pos_list[counter])
        print("Нейтрально:", neu_list[counter])
        print("################################")
        print()
        counter+=1

        print("ВЫЧИСЛЕНИЕ ТОЧЕК МАКСИМУМА И МИНИМУМА ВХОЖДЕНИЯ В САРКАЗМ")
        print("##########################")
        print(znachenie_list)
        max_sarc_list = max(znachenie_list)
        min_sarc_list = min(znachenie_list)
        print("Максимальное значение сарказма", "(x"+f"{max_x_index}"+"):", max_sarc_list,)
        print("Минимальное значение сарказма", "(x"+f"{min_x_index}"+"):", min_sarc_list)
        print("##########################")

        #ТОКЕНИЗАЦИЯ
        #tokens = word_tokenize(" ".join(sentence))
        #print("ТОКЕНЫ: ", tokens)


def preprocess_big_text():
    split_text = big_text.split(".")
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
        no = 0
        vot = 0
        esli = 0
        for word in list_parts:
            if word == "не":
                no += 1
            else:
                if word == "вот":
                    vot += 1
                elif word == "если":
                    esli += 1

        form_xs = list()
        if len_text != 0:

            # ПЕРЕМЕННАЯ Х1 - КОЛИЧЕСТВО ЗАГЛАВНЫХ БУКВ
            for s in sentence:
                if s.isupper():
                    sum1 += 1
            count_uppercase = sum1
            # Вычисление эталона заглавных букв
            x1 = round(count_uppercase / len_text, 4)
            print(f"\nПеременная x1 (верхний регистр) = {round(x1, 4)}")
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
        print("СЧЁТЧИК ЧАСТИЦ 'НЕ, ВОТ, ЕСЛИ'")
        print("#############################")
        print('Количество "Не" в предложенни:', no)
        print('Количество "Вот" в предложенни:', vot)
        print('Количество "Если" в предложенни:', esli)
        print("#############################")
        print()





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

    for word in words:
        filtered_tokens.append(word)

    fdist = FreqDist(filtered_tokens)
    print()
    print("ЧАСТОТА СЛОВ")
    print("########################")
    print(*fdist.most_common(len(filtered_tokens)), sep='\n')
    print("########################")
    print()




def morph_analyzer():
    text = fifteen()
    #preproc = preprocess(text)
    big_text = preprocess_big_text()
# @classmethod

morph_analyzer()
