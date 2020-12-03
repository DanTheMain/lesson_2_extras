# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vouls_count = 0
for char in list(word.lower()):
    if char in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'ю', 'я'):
        vouls_count += 1
print(vouls_count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
print(len(sentence.replace(' ', ''))/len(sentence.split()))
2 + 8 + 1 + 5