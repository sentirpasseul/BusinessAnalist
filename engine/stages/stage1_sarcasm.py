import random
import re
split_regex = re.compile(r'[|!|?|…]')


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
    for s in range(form_15):
        print(list_text[s])





fifteen()