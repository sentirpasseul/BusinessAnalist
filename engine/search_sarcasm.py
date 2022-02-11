file = open(r'test.txt', 'r', encoding='utf-8')
f = "\n\n".join(file.read().splitlines())
print(f)

