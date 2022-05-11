from engine_algorythm import *
from get_text import *

def input_text():
    count_sentence1 = 0
    text_input = input("Введите свой текст: ")

    if text_input.count("\n") > 1:
        # print("Строчек больше 1")
        count_sentence1 = text_input.count("\n")

    else:
        # print("Строчек меньше двух")
        count_sentence1 = text_input.count(".")

    print("Количество предложений:", count_sentence1)
    return text_input, count_sentence1

def strings_sarc(count_sentences):
    txt = f_sarc2
    split = txt.split("\n")
    l1 = []
    list1 = []
    for s in split:
        list1.append(s)
    for s in range(count_sentences):
        l1.append(list1[s])
    #print(l1)
    return "".join(l1)

def strings_nsarc(count_sentences):
    txt = f_witcher
    split = txt.split("\n")
    l1 = []
    list1 = []
    for s in split:
        list1.append(s)
    for s in range(count_sentences):
        l1.append(list1[s])
    #print(l1)
    return "".join(l1)

def algorythm():
    ds_sarc = f_sarc2
    ds_nsarc = f_witcher
    ds_wiki_sarc = f_wiki_sarc
    ds_nsarc2 = f_nsarc2


    text_input, count_sentences = input_text()
    text_sarc = strings_sarc(count_sentences)
    text_nsarc = strings_nsarc(count_sentences)

    print("INPUT")
    process_input = Algorythm(text_input).analyzer()
    print("Значение по формуле: ", process_input)

    print("SARCASM")
    process_sarc = Algorythm(text_sarc).analyzer() / 2
    print("Значение по формуле: ", process_sarc)

    print("NOT SARCASM")
    process_nsarc = Algorythm(text_nsarc).analyzer() / 2
    print("Значение по формуле: ", process_nsarc)

    #if process_sarc < process_nsarc and process_input > process_sarc:
     #   print("Текст саркастичный")
    print(int(process_nsarc))

    if (int(process_sarc) == int(process_input)):
        print("Текст саркастичный")
    elif (int(process_nsarc) == int(process_input)):
        print("Текст не саркастичный")
    elif int(process_nsarc) == int(process_input) != int(process_sarc):
        print("Текст неоднозначный")
    else:

        if process_input >= process_sarc:
            print("Текст саркастичный")
        elif process_nsarc < process_input < process_sarc:
            print("Текст саркастичный")
        elif process_nsarc < process_nsarc:
            if process_sarc <= process_input:
                print("Текст саркастичный")
        elif process_input <= process_nsarc:
            print("Текст не саркастичный")
        #elif process_input == process_nsarc == process_sarc:
         #  print("Текст неоднозначный, значения равны")

    return process_input

algorythm()


