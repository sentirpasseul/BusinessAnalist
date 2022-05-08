from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import fasttext

fasttext.FastText.eprint = lambda x: None
FastTextSocialNetworkModel.MODEL_PATH = 'fasttext-social-network-model.bin'

def tonality(del_sym: list):
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