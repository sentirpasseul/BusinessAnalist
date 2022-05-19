import re
import string

from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import fasttext

fasttext.FastText.eprint = lambda x: None
FastTextSocialNetworkModel.MODEL_PATH = 'fasttext-social-network-model.bin'

def tonality(del_sym: list):
    fasttext.FastText.eprint = lambda x: None
    FastTextSocialNetworkModel.MODEL_PATH = 'fasttext-social-network-model.bin'
    l2 = [x for x in range(100)]
    for i in range(len(del_sym)):
        if del_sym[i] == l2:
            del_sym.remove(del_sym[i])

    tokenizer = RegexTokenizer()
    model = FastTextSocialNetworkModel(tokenizer=tokenizer)

    results = model.predict(del_sym, k=4)
    neu_list = list()
    neg_list = list()
    pos_list = list()

    print(del_sym)
    for sentence, sentiment in zip(del_sym, results):

        if sentence != string.digits:

            # Анализ Тональности предложения
            neu = sentiment.get('neutral')
            p = sentiment.get('positive')
            neg = sentiment.get('negative')





            neu_list.append(neu)
            pos_list.append(p)
            neg_list.append(neg)


    for s in range(len(neg_list)):
        if neg_list[s] is None:
            neg_list[s] = 0
    for s in range(len(neu_list)):
        if neu_list[s] is None:
            neu_list[s] = 0
    for s in range(len(pos_list)):
        if pos_list[s] is None:
            pos_list[s] = 0



        #print(sentence, '\n',
         #     'neutral = ', sentiment.get('neutral'), '\n',
          #    'positive = ', sentiment.get('positive'), '\n'
           #   'negative = ', sentiment.get('negative'), '\n'
            #  )

    return neg_list,neu_list,pos_list