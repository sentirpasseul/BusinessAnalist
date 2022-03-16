import re
from engine.preprocessing.input_text import f
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess(text):
    text = text.lower().replace("ё", "е")
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)
    text = re.sub('@[^\s]+', 'USER', text)
    text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
    text = re.sub(' +', ' ', text)
    return text.strip()
preprocess(f)
print("1. Вывод текста: ")
print()
print(f)
print()


"""
ru_stopwords = stopwords.words('russian')
tokens = word_tokenize(sub1, language='russian')
filtered_tokens = []
for token in tokens:
    if token not in ru_stopwords:
        filtered_tokens.append(token)


print("5. Удаление стоп-слов:")
print(filtered_tokens)
print()
"""
i = 0
print("Текст строками: ")
filtered_tokens_list = []
while i <= len(sub1):
        filtered_tokens_list.append(sub1[i])
        print(" ".join(sub1[i:i+20]), end="\n")
        i += 20
print(filtered_tokens_list)

filtered_tokens_file = open(r'filtered_tokens.txt', 'w')
for i in range(len(filtered_tokens_list)):
    filtered_tokens_file.write("\n".join(filtered_tokens_list[i:i+20]))

