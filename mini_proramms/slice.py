# В решении этой задачи практикуюсь на срезах. Суть задачи: есть два друга гооворящие на вымышленной языке - Pig Latin
# в котором первая буква слова переносится в конец, далее добавляется 'ay'. road = oadray
# Задача: дана фраза произвольной длины на английском, которую надо перевести на Pig Latin, к примеру:
# Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium

phrase = input()

lst = phrase.split()    #разделение строки на подстроки(слова). По умлочанию, в качестве разделителя выбран пробел

n_word = None   # Слово на Pig Latin
new_phrase = '' # Новая фраза с учетом изменений

for word in lst:    # Цикл перебирающий каждый фрагмент а lst
    n_word = word[1:] + word[0] + 'ay ' # Генерация нового слова
    new_phrase = new_phrase + n_word
print(new_phrase)
