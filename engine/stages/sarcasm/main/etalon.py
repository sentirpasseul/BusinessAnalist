from engine_algorythm import *
from pathlib import Path
from get_text import *


def input_text(text_input):
    count_sentence1 = 0
    #text_input = input("Введите свой текст: ")
    """
    if text_input.count("\n") == text_input.count("."):
        # print("Строчек больше 1")
        count_sentence1 = text_input.count("\n")

    else:
        # print("Строчек меньше двух")
        count_sentence1 = text_input.count(".")
    """
    count_sentence1 = text_input.count(".")
    print("Количество предложений:", count_sentence1)
    return count_sentence1

def strings_sarc(count_sentences, txt):

    split = txt.split(".")
    l1 = []
    list1 = []
    for s in split:
        list1.append(s)
    for s in range(count_sentences):
        l1.append(list1[s])
    #print("STRING SARC")
    #print(l1)
    return l1

def algorythm():
    dataset_input = input("Пожалуйста, введите свой текст:")
    c_s_sarc = input_text(dataset_sarcasm)
    #c_s_nsarc = input_text(dataset_notsarc)
    c_s_input = input_text(dataset_input)


    text_split_sarc = strings_sarc(c_s_input, dataset_sarcasm)
    #text_split_nsarc = strings_sarc(c_s_nsarc, dataset_notsarc)
    text_split_input = strings_sarc(c_s_input, dataset_input)


    #print("INPUT")
    #process_input = Algorythm(text_input_sarc).analyzer()
    #print("Значение по формуле: ", process_input)

    #print("SARCASM")
    process_sarc, df_sentences_sarc, form_sarc = Algorythm(text_split_sarc).analyzer()
    #process_nsarc, df_sentences_nsarc, form_nsarc = Algorythm(text_split_nsarc).analyzer()
    process_input, df_sentences_input, form_input = Algorythm(text_split_input).analyzer()

    #filepath_sarc = Path('src/created_datasets/dataset_sarc.csv').parent.mkdir(parents=True, exist_ok=True)
    #filepath_nsarc = Path('src/created_datasets/dataset_nsarc.csv').parent.mkdir(parents=True, exist_ok=True)

    #df_sentences_sarc.to_csv(filepath_sarc)
    #df_sentences_nsarc.to_csv(filepath_nsarc)
    #df_sentences_input.to_csv('/src/created_datasets/dataset_input.csv')

    #print(process_sarc)
    #print(process_nsarc)
#    print(process_input)

    #print("Формула Сарказма:", form_sarc)
    #print("Формула Обычного:", form_nsarc)
    #print("Формула вводимого текста:", form_input)

    if form_input >= form_sarc:
        print("Текст саркастичный")
    elif form_input < form_sarc:
        print("Текст не саркастичный")






    #print("NOT SARCASM")
    #process_nsarc = Algorythm(text_split_nsarc).analyzer() / 2
    #print("Значение по формуле: ", process_nsarc)

    #print("Анализ тональности", Algorythm(text_input_sarc).analyzer())

    """
    if process_sarc < process_nsarc and process_input > process_sarc:
        print("Текст саркастичный")
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
        elif process_input == process_nsarc == process_sarc:
           print("Текст неоднозначный, значения равны")

    #return process_input
    """
algorythm()


