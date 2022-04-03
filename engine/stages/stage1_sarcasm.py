import random
import re
split_regex = re.compile(r'[|!|?|…]')
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel, FastTextToxicModel
import fasttext
import pandas as pd
import numpy as np
import sklearn

fasttext.FastText.eprint = lambda x: None
FastTextSocialNetworkModel.MODEL_PATH = 'fasttext-social-network-model.bin'

file = open(f'data.txt', 'r', encoding="utf-8")
text = file.read()
#only_text = re.sub(r'[\d]', '', text)


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
    for s in range(form_15):
        ar_15.append(list_text[s])
    return ar_15

def Question(s):
    for symbol in s:
        if "?" in symbol:
            d = True

#def neutral():


def math_model():
    ar_15 = fifteen()

    tokenizer = RegexTokenizer()

    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    messages = [
        'привет',
        'я люблю тебя!!',
        'малолетние дебилы'
    ]



    results = model.predict(ar_15, k=4)

    for message, sentiment in zip(ar_15, results):
        # привет -> {'speech': 1.0000100135803223, 'skip': 0.0020607432816177607}
        # люблю тебя!! -> {'positive': 0.9886782765388489, 'skip': 0.005394937004894018}
        # малолетние дебилы -> {'negative': 0.9525841474533081, 'neutral': 0.13661839067935944}]
        print(message, '\n',
              'neutral = ', sentiment.get('neutral'), '\n',
              'positive = ', sentiment.get('positive'), '\n'
              'negative = ', sentiment.get('negative'))
math_model()