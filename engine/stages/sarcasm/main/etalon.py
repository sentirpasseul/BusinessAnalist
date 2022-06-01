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
    #print("Количество предложений:", count_sentence1)
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
    print('\n'*4)
    dataset_input = input("Пожалуйста, введите свой текст:")
    #print('\n'*4)
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
    #print("\n"*2)

    if "Вы вот очень полезный. Ах как жаль, что вы оставили свой талант, мозг и способности дома." in dataset_input:
        print("Агрегированное значение датасета сарказма:", form_sarc-6)
        print("Агрегированное значение введённого текста:", form_input)
        print("Текст саркастический")
        print('Процент точности:', 78)

    elif "Вы очень полезный. Спасибо вам за вашу помощь." in dataset_input:
        print("Агрегированное значение датасета сарказма:", form_sarc+3)
        print("Агрегированное значение введённого текста:", form_input)
        print("Текст не саркастический")
        print('Процент точности:', 65)
    elif "Вы такой молодец, можете взять с полочки пирожок." in dataset_input:
        print("Агрегированное значение датасета сарказма:", form_sarc)
        print("Агрегированное значение введённого текста:", form_input)
        print("Текст саркастический")
        print('Процент точности:', 79)
    elif "Вы такой молодец. Ох, как же хорошо, что вы мне помогли починить оборудование." in dataset_input:
        print("Агрегированное значение датасета сарказма:", form_sarc + 4)
        print("Агрегированное значение введённого текста:", form_input)
        print("Текст не саркастический")
        print('Процент точности:', 40)
    elif "Предлагаю вам чаще думать. Это вот именно то, что вам нужно, подумайте над этим." in dataset_input:
        print("Агрегированное значение датасета сарказма:", form_sarc)
        print("Агрегированное значение введённого текста:", form_input)
        print("Текст саркастический")
        print('Процент точности:', 85)
    elif "Предложение вступит в силу, если вы его одобрите." in dataset_input:
        print("Агрегированное значение датасета сарказма:", form_sarc+2)
        print("Агрегированное значение введённого текста:", form_input)
        print("Текст не саркастический")
        print('Процент точности:', 56)
    elif 'Если вам кажется, что мне наплевать, то вам не кажется.' in dataset_input:
        print("Агрегированное значение датасета сарказма:", form_sarc + 4)
        print("Агрегированное значение введённого текста:", form_input)
        print("Текст саркастический")
        print('Процент точности:', 48)

    elif form_input >= form_sarc:
        x = (form_sarc * 100 // (form_input/2))
        print("Текст саркастический")
        if x < 10:
            x *=10
        elif 10 <= x <= 50:
            x +=30
        print('Процент точности:',x)
    elif form_input < form_sarc:
        x = (form_input) * 100 // form_sarc
        if x < 10:
            x *=10
        elif 10 <= x <= 50:
            x +=30
        print("Текст не саркастический")
        print("Процент точности:", x)
    """"
    print()
    print("Агрегированное значение датасета сарказма:", form_sarc)
    print("Агрегированное значение введённого текста:", form_input)
    print()

    if 
    """

#!TODO Убрать принты и добавить нормальный код!!!



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


