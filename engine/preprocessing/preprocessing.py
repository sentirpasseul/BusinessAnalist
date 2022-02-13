import re
from engine.preprocessing.input_text import f
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

print("1. Вывод текста: ")
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

