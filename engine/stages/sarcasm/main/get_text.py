file = open(f'data.txt', 'r', encoding="utf-8")
dataset_sarcasm = file.read()

file_big_text = open(f'test.txt', 'r', encoding='utf-8')
dataset_notsarc = file_big_text.read()

file_test2 = open(f'test2.txt', 'r', encoding='utf-8')
test2 = file_test2.read()

file_witcher = open(f'etalons/etalon_notsarc', 'r', encoding='utf-8')
f_witcher = file_witcher.read()

file_sarc = open(f'etalons/etalon_sarc', 'r', encoding='utf-8')
f_sarc2 = file_sarc.read()

file_wiki_sarc = open(f'etalons/wiki_sarc.txt', 'r', encoding='utf-8')
f_wiki_sarc = file_wiki_sarc.read()

file_nsarc2 = open(f'etalons/nsarc2.txt', 'r', encoding='utf-8')
f_nsarc2 = file_nsarc2.read()
