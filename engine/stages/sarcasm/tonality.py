from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
import fasttext
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

fasttext.FastText.eprint = lambda x: None
FastTextSocialNetworkModel.MODEL_PATH = 'fasttext-social-network-model.bin'

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)
"""""
##Распознавание тональности текста

def get_prec():
    text = fifteen()
    del_sym = preprocess_text(text).split("\n")
    print(del_sym)
    for sentence in del_sym:
        # Сплитим предложение на слова
        sent1 = sentence.split(" ")
        list_parts = []

        print()
        # Разбиваем спличенный текст на токены
        sub1_reset = word_tokenize(" ".join(sent1))

        tokenize_sentence = word_tokenize(" ".join(sent1))
        results = model.predict(sub1_reset, k=4)
        res_ton = dict
        return sentence, results
def tonality():
    sentence, results = get_prec()
    for sentence, sentiment in zip(sentence, results):
        # Анализ Тональности предложения
        neu = sentiment.get('neutral')
        p = sentiment.get('positive')
        neg = sentiment.get('negative')

        print(sentence, '\n',
              'neutral = ', sentiment.get('neutral'), '\n',
              'positive = ', sentiment.get('positive'), '\n'
              'negative = ', sentiment.get('negative'), '\n'
            )

        # return neu, p, neg
"""""