import re

from tonality import tonality
#from ui.main_ui import input_text
import nltk.downloader
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from collocations import *
import pandas as pd
import numpy as np
import pymorphy2
from pydub import AudioSegment
from pydub.playback import play
import statistics

split_regex = re.compile(r'[|!|?|…]')
morph = pymorphy2.MorphAnalyzer()
nltk.downloader.Downloader('webtext')

class Algorythm():

    def __init__(self, text):
        self.__col_if = "".join(collocations_if)
        self.__col_bi = "".join(collocations_bi)
        self.__col_no = "".join(collocations_no)
        self.__text = text


        #print("!"*50)
        if text.count("\n") == text.count("."):
            #print("Строчек больше 1")
            self.__count_sentence = text.count("\n")
            self.__split_text = text
        else:
            #print("Строчек меньше двух")
            self.__count_sentence = text.count(".")
            self.__split_text = text.split(".")
        self.__neg_list, self.__pos_list, self.__neu_list = tonality(self.__split_text)
        #print(self.split_text)
        #print(self.count_sentence)

    def get_col_if(self):
        return self.__col_if




    def preprocess(self):
        text = self.__text
        # vis = vizual_ton(split_text, neg_list, pos_list, neu_list)
        counter = 0
        znachenie_list = list()

    def analyzer(self):
        text = self.__text
        #w2v_model = Word2Vec(min_count=10, window=2, negative=10, alpha=0.03, min_alpha=0.0007, sample=6e-5, sg=1)
        ##w2v_model.build_vocab(dict1)
        #w2v_model.train(dict1, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
        #w2v_model.init_sims(replace=True)

        #dict = {'Sentence': self.split_text, 'Негативно': self.neg_list, "Позитивно": self.pos_list, "Нейтрально": self.neu_list}

        #df = pd.DataFrame(dict)
        #print(df)
        #print(df_width)
        colls = 0

        count_if = 0
        sentences_ton = list()
        count_bi = 0        #количество бы
        count_zap_no = 0    #количество ", но"
        count_interj = 0    #количество междометий
        count_advb = 0      #количество наречий
        count_adjf = 0      #количество полных прилагательных
        count_adjs = 0      #количество кратких прилагательных




        x_norm = 0
        x_norm_list = list()
        z_norm = 0
        z_norm_list = list()
        """"
        print("ТОНАЛЬНОСТЬ")
        print(self.pos_list)
        print(self.neg_list)
        print(self.neu_list)

        print(self.split_text)
        """""
        list_sentenses = []
        count1 = 0

        for sentence in self.__split_text:

                if "\n" in sentence:
                    sentence = re.sub("\n", "", sentence)

                #Счётчик по предложениям
                #Медиана тональности (смещение)
                median1 = statistics.median([self.__neg_list[count1], self.__neu_list[count1], self.__pos_list[count1]])

                #
                list_ton = self.__pos_list[count1], self.__neu_list[count1], self.__neg_list[count1]

                sum1 = statistics.mean(list_ton)
                z_norm = (sum1 - min(list_ton)) / max(list_ton) - min(list_ton)
                z_norm_list.append(abs(z_norm))
                count1 +=1



                reg_sent = re.sub("[\d+]", "", sentence)
                list_sentenses.append(reg_sent)





                colls = 0
                #print(w2v_model.wv.most_similar(positive=[f"{sentence}"]))
                if self.__col_if in sentence:
                    count_if +=1
                    #print("ЕСТь")
                if self.__col_bi in sentence:
                    count_bi +=1
                if self.__col_no in sentence:
                    count_zap_no +=1
                if "кажется, что" in sentence:
                    colls +=1
                if "не кажется" in sentence:
                    colls +=1

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
                        #print(f"Для слова '{word}' частью речи является '{part}'")

                        # Сплитим строку из морф анализа
                        morph_split = "".join(part).split(",")
                        #print(morph_split)



                count_interj += list_parts.count("МЕЖД")
                count_advb += list_parts.count("НАР")
                count_adjf += list_parts.count("ПРИЛ")
                count_adjs += list_parts.count("КР_ПРИЛ")
                #self.count_bi = sentence.count("бы")
               # self.count_zap_no = sentence.count(', но')


                neg_sent, pos_sent, neu_sent = tonality(sentence)

                #sum_neg_sent = math.fsum(neg_sent)
                #sum_pos_sent = math.fsum(pos_sent)
                #sum_neu_sent = math.fsum(neu_sent)

                #print()
                #print("Отрицательно:", sum_neg_sent)
                #print("Положительно:", sum_pos_sent)
                #print("Нейтрально:", sum_neu_sent)
                #print()

                #print("Количество БЫ:", count_bi)
                #print("Количество ', но'", count_zap_no)

                #print()
                #print("АНАЛИЗ ТОНАЛЬНОСТИ ПРЕДЛОЖЕНИЯ:")
                #print("###############################")
                #print("Отрицательно:", neg_list[counter])
                #print("Положительно:", pos_list[counter])
                #print("Нейтрально:", neu_list[counter])
                #print("################################")
                #print()
                #counter += 1




        for i in list_sentenses:
            if i == "":
                list_sentenses.remove(i)

        #print(list_sentenses)
        data_sentences = {"Предложения": list_sentenses, "Негативно": self.__neg_list, "Позитивно": self.__pos_list,
                          "Нейтрально": self.__neu_list, "Z-нормализация": z_norm_list}




        df_sentences = pd.DataFrame(data_sentences)



        pd.options.display.max_rows = 999
        pd.set_option('display.width', 1000)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.max_colwidth',250)
        print()
        print("ДАТА ФРЕЙМ")
        print(df_sentences)
        print()

        """
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
        """


        #print("СЧЁТЧИК ВСЕХ ПРЕДЛОЖЕНИЙ В ТЕКСТЕ")
        #print(self.__count_sentence)

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
        words = " ".join(self.__split_text).split(" ")
        count_q = words.count('"')
        if count_q > 0:
            count_q = True

        for word in words:
            filtered_tokens.append(word)

        fdist = FreqDist(filtered_tokens)
        #print()
        #print("ЧАСТОТА СЛОВ")
        #print("########################")
        #print(*fdist.most_common(len(filtered_tokens)), sep='\n')
        #print("########################")
        #print()
        #fdist.plot(15)


        """
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
        """

        x1 = sum([words.count("не"), words.count("вот"),
                  words.count("если"), count_if, count_bi,
                  count_zap_no, words.count("что")])
        print('Х1 - количество лексем ("но", "вот", "если", "бы", "что"):', x1)

        x2 = sum([count_interj, count_adjf, count_advb, count_adjs])
        print("Х2 - количество междометий:",x2)

        x_all = x1, x2
        x_sum = sum([x1, x2])

        x_mean = statistics.mean(x_all)
        try:
            statAn = (x_sum - min(x_all)) / max(x_all) - min(x_all)
        except ZeroDivisionError:
            statAn = 0
        stat_z = sum(z_norm_list)
        #print("STAT_Z", stat_z)
        all_params = [statAn, stat_z]
        params_mean = statistics.mean(all_params)

        print("Статистический анализ текста:", stat_z)
        #цprint('Агрегированное значени дистанции каждого слова:', )
        #print("params_mean", params_mean)
        #print("np.std(all_params)", np.std(all_params))

        try:
            formula = abs(stat_z - params_mean / np.std(all_params))
            print("Вычисление значения всех весовых коэффициентов:", formula)
            #if formula < 0:
            #formula = (stat_z - min(all_params)) / max(all_params) - min(all_params)
        except ZeroDivisionError:
            formula = 0




        #print("!"*50)

        #model_words = corpora.Dictionary(filtered_tokens)
        #print(model_words)

        try:
            sound = AudioSegment.from_file('iphone.wav', format='wav')
            play(sound)
        except RuntimeWarning:
            print("")
        return statAn, df_sentences, formula











