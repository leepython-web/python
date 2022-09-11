file = open('eggs.txt', 'r', encoding='utf-8')
content = file.readlines()
for line in content:
    print(line)
