t = "СТОП"
text = ""
while t != text:
    file_sarc = open('dataset_sarc.txt', 'a+')
    with file_sarc:
            text = input("Введите предложение: ")
            if text != "СТОП":
                file_sarc.write(text + '\n')
            else:
                break