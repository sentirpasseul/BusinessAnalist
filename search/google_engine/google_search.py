import googlesearch
from googlesearch import search
from search.input_search import input_search

filtered = []
for item in search(input_search, tld='co.in', num=10, stop=10, pause=2, lang='ru'):
    filtered.append(item)
    print(item)

#TODO Нужно сделать проверку на адрес вк, то есть проверку на url
for item in filtered:
    filt1 = "" .join(filtered[item])
    print(filt1)