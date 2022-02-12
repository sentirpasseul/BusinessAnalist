import googlesearch
from googlesearch import search
from search.input_search import input_search

for item in search(input_search, tld='co.in', num=10, stop=10, pause=2):
    print(item)