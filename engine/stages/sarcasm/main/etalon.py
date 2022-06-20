from engine_algorythm import *
from pathlib import Path
from get_text import *


def input_text(text_input):

    count_sentence1 = text_input.count(".")
    return count_sentence1

def strings_sarc(count_sentences, txt):

    split = txt.split(".")
    l1 = []
    list1 = []
    for s in split:
        list1.append(s)
    for s in range(count_sentences):
        l1.append(list1[s])
    return l1

def algorythm():
    print('\n'*4)
    dataset_input = input("Пожалуйста, введите свой текст:")
    c_s_sarc = input_text(dataset_sarcasm)
    c_s_input = input_text(dataset_input)


    text_split_sarc = strings_sarc(c_s_input, dataset_sarcasm)
    text_split_input = strings_sarc(c_s_input, dataset_input)


    #print("INPUT")
    #process_input = Algorythm(text_input_sarc).analyzer()

    #print("SARCASM")
    process_sarc, df_sentences_sarc, form_sarc = Algorythm(text_split_sarc).analyzer()
    #process_nsarc, df_sentences_nsarc, form_nsarc = Algorythm(text_split_nsarc).analyzer()
    process_input, df_sentences_input, form_input = Algorythm(text_split_input).analyzer()

    print("Значение по формуле: ", process_input)
    #filepath_sarc = Path('src/created_datasets/dataset_sarc.csv').parent.mkdir(parents=True, exist_ok=True)
    #filepath_nsarc = Path('src/created_datasets/dataset_nsarc.csv').parent.mkdir(parents=True, exist_ok=True)

    df_sentences_sarc.to_csv('/src')
    #df_sentences_nsarc.to_csv(filepath_nsarc)
    df_sentences_input.to_csv('/stages/sarcasm/main/etalons/dataset_input.csv')

    print(process_sarc)


    print()
    print("Агрегированное значение датасета сарказма:", form_sarc)
    print("Агрегированное значение введённого текста:", form_input)
    print()

    if process_input >= process_sarc:
        print("Текст саркастичный")
        x = (form_sarc * 100 // (form_input/2))
        print("Процент точности:", x)
    elif (process_input<process_sarc):
        x = (form_input) * 100 // form_sarc
        print("Текст не саркастичный")
        print("Процент точности:", x)

algorythm()


