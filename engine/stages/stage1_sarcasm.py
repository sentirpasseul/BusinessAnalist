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

    #Каждое предложение прогоняем по MorphAnalyzer
    for sentence in del_sym:
        #Сплитим предложение на слова
        sent1 = sentence.split(" ")
        list_parts = []
        #Разбиваем спличенный текст на токены
        sub1_reset = word_tokenize(" ".join(sent1))
        if sub1_reset != " " and sub1_reset !="":
            print(sub1_reset)

        #Анализируем каждое слово в предложении
        for word in sent1:
            if word != "":
                parse_parts = morph.parse(word)[0]
                part = parse_parts.tag.cyr_repr
                list_parts.append(part)
                print(f"Для слова '{word}' частью речи является '{part}'")

    #СЧЁТЧИК ВСЕХ СЛОВ В ТЕКСТЕ
        len_text = len(sub1_reset)
        print("\nСчётчик всех слов в тексте:", len_text, sep="\n")

        #ТОКЕНИЗАЦИЯ
        #tokens = word_tokenize(" ".join(sentence))
        #print("ТОКЕНЫ: ", tokens)


    #ОПРЕДЕЛЕНИЕ ЧАСТЕЙ РЕЧИ





def morph_analyzer():
    text = fifteen()
    preproc = preprocess(text)
# @classmethod

#@classmethod
def parts_speech():
    list_text = (text.split('\n'))
    print(list_text)

    # @classmethod
def math_model():
        tonality = ton()

# math_model()
# print(parts_speech())
morph_analyzer()

