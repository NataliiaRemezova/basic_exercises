# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
count = 0
for symbol in word:
    if symbol.lower() == 'а':
        count += 1
print(count)

# Вывести количество гласных букв в слове
word = 'Архангельск'
vokal = ["а", "е", "ё", "и", "о", "у", "э", "ю", "я"]
count = 0
for symbol in word:
    if symbol.lower() in vokal:
        count += 1
print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# count = 1
# for symbol in sentence:
#     if symbol.isspace():
#         count += 1
print(len(sentence.split()))



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sum = 0
for word in sentence:
    sum += len(word)
print(sum / len(sentence.split()))
