import math
import re
import string

import nltk.downloader
from get_text import *
from engine_algorythm import *
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import fasttext
import pymorphy2

split_regex = re.compile(r'[|!|?|…]')
morph = pymorphy2.MorphAnalyzer()
nltk.downloader.Downloader('webtext')

fasttext.FastText.eprint = lambda x: None
FastTextSocialNetworkModel.MODEL_PATH = 'fasttext-social-network-model.bin'


#only_text = re.sub(r'[\d]', '', text)

#class check_sarc():

# @staticmethod
def Question( s):
    for symbol in s:
        if "?" in symbol:
            d = True

#@staticmethod

def split_big_text():
    list_text = (dataset_notsarc.split('.'))
    return list_text

def preprocess_text(text1):
    text1 = " ".join(text1).lower().replace("ё", "е")
    text1 = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text1)
    text1 = re.sub('@[^\s]+', 'USER', text1)
    text1 = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text1)
    text1 = re.sub(' +', ' ', text1)
    text1 = re.sub('([0-9])', "\n", text1)
    return text1.strip()



def no_dig():
    file = open('test.txt', 'r', encoding='utf-8')
    f = file.read()
    fis = re.sub("[\d]", "", f)


def count_quot():
    split_text = dataset_notsarc.split(".")

def morph_analyzer():
    #preproc = preprocess(text)
    big_text = preprocess_big_text()
# @classmethod

morph_analyzer()

