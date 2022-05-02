from engine_algorythm import *




def algorythm():
    ds_sarc = f_sarc2
    ds_nsarc = f_witcher

    print("ТЕКСТ С САРКАЗМОМ")
    process_sarc1 = preprocess_big_text(ds_sarc)
    print("ТЕКСТ БЕЗ САРКАЗМА")
    process_nsarc1 = preprocess_big_text(ds_nsarc)


    return process_sarc1, process_nsarc1

algorythm()


