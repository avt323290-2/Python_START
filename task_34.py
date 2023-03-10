# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам

# Сначала определяем функцию, которая будет считать количество гласных в слове
def count_vowels(word):
    vowels = "аеёиоуыэюя" # список гласных букв
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count

# Теперь просим пользователя ввести стихотворение
poem = input("Введите стихотворение: ")

# Разбиваем стихотворение на фразы, используя пробелы в качестве разделителя
phrases = poem.split()

# Получаем количество гласных в каждой фразе и записываем в список
vowel_counts = []
for phrase in phrases:
    words = phrase.split("-") # Разбиваем фразу на слова, используя дефисы в качестве разделителя
    phrase_vowels = sum(count_vowels(word) for word in words) # Считаем количество гласных во всех словах фразы
    vowel_counts.append(phrase_vowels)

# Проверяем, все ли значения в списке vowel_counts одинаковые
if vowel_counts.count(vowel_counts[0]) == len(vowel_counts):
    print("С ритмом все в порядке! Парам пам-пам")
else:
    print("Ритма нет! Пам парам")
