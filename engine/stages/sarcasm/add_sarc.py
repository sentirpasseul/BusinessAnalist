from nltk.tokenize import word_tokenize

def preproc():
    file = open('main/data.txt', 'r', encoding="utf-8")
    text = file.read()
    split_text = text.split(f"{str.isdigit}")
    tok = word_tokenize(" ".join(split_text), "russian")
    print(tok)
    #print(" ".join(split_text))

t = "СТОП"
text = ""
while t != text:
    file_sarc = open('main/dataset_sarc.txt', 'a+')
    with file_sarc:
            text = input("Введите предложение: ")
            if text != "СТОП":
                file_sarc.write(text + '\n')
            else:
                preproc()
