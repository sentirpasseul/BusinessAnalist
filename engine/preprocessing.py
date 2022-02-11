import re
from input_search import f
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


print("1. Считывание текста: ")
print()
print(f)
print()

f_lower = f.lower()
print("2. Данные в нижнем регистре:")
print(f_lower)
print()

space = re.sub(r'\s+', ' ', f_lower)
print("3. Удаление лишних пробелов:")
print(space)



print("4. Удаление знаков препинания: ")
sub1 = re.sub(r'[^\w\s]',' ', space)
print(sub1)


ru_stopwords = stopwords.words('russian')
tokens = word_tokenize(sub1, language='russian')
filtered_tokens = []
for token in tokens:
    if token not in ru_stopwords:
        filtered_tokens.append(token)


print("5. Удаление стоп-слов:")
print(filtered_tokens)
print()

i = 0
print("Текст строками: ")
while i <= len(filtered_tokens):
        print(" ".join(filtered_tokens[i:i+20]), end="\n")
        i += 20
print()