from engine_algorythm import *
from get_text import *




def algorythm():
    ds_sarc = f_sarc2
    ds_nsarc = f_witcher
    ds_wiki_sarc = f_wiki_sarc
    ds_nsarc2 = f_nsarc2

    #print("ТЕКСТ С САРКАЗМОМ")
    process_sarc1 = analyzer(ds_sarc)
    #print("ТЕКСТ БЕЗ САРКАЗМА")
    process_nsarc1 = analyzer(ds_nsarc)

    print("Текст сарказма из Википедии")
    print()
    process_wiki_sarc = analyzer(ds_wiki_sarc)

    print("Текст без сарказма")
    print()
    p_nsarc2 = analyzer(ds_nsarc2)

    return process_sarc1, process_nsarc1, process_wiki_sarc, p_nsarc2

algorythm()


