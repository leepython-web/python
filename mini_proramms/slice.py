# В решении этой задачи практикуюсь на срезах. Суть задачи: есть два друга гооворящие на вымышленной языке - Pig Latin
# в котором первая буква слова переносится в конец, далее добавляется 'ay'. road = oadray
# Задача: дана фраза на английском, которую надо перевести на Pig Latin
# Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium
phrase = input()
lst = phrase.split()
n_word = None
new_phrase = ''

for word in lst:
    n_word = word[1:] + word[0] + 'ay '
    new_phrase = new_phrase + n_word
print(new_phrase)
