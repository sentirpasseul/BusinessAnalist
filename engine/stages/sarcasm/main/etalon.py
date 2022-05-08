from engine_algorythm import *
from get_text import *




def algorythm():
    ds_sarc = f_sarc2
    ds_nsarc = f_witcher
    ds_wiki_sarc = f_wiki_sarc
    ds_nsarc2 = f_nsarc2

    #print("ТЕКСТ С САРКАЗМОМ")
    process_sarc1 = Algorythm(ds_sarc).analyzer()
    #print("ТЕКСТ БЕЗ САРКАЗМА")
    process_nsarc1 = Algorythm(ds_nsarc).analyzer()

    print("Текст сарказма из Википедии")
    print()
    process_wiki_sarc = Algorythm(ds_wiki_sarc).analyzer()

    print("Текст без сарказма")
    print()
    p_nsarc2 = Algorythm(ds_nsarc2).analyzer()

    return process_sarc1, process_nsarc1, process_wiki_sarc, p_nsarc2

algorythm()


