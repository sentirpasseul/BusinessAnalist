file = open(f'data.txt', 'r', encoding="utf-8")
dataset_sarcasm = file.read()

file_big_text = open(f'test.txt', 'r', encoding='utf-8')
dataset_notsarc = file_big_text.read()

file_test2 = open(f'test2.txt', 'r', encoding='utf-8')
test2 = file_test2.read()