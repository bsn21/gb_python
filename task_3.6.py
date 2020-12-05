# 6. Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

print('--1--')
# 1) Вариант - простой вариант без поиска букв предложения

def int_func(word):
    word = word.title()
    return word

print(int_func('text'))
print(int_func('my sentence is very long'))

print('--2--')
# 2) Вариант - более сложный вариант с поиском букв предложения в letters

def int_func(word):
    letters = 'abcdefghijklmnoopqrstuvwxyz'
    if set(word).difference(letters):
        return False
    else:
        return word.title()

sentence = input('Введите строку из слов, разделенных пробелами: ').split()
for el in sentence:
    print(int_func(el), end=' ') # выводит False если в слове из предложения нет букв из letters

print('\n--3--')
# 3) Вариант - то же, что и вариант 2, return в одну строку

def int_func(word):
    letters = 'aabbccdefghijklmnoopqrstuvwxyz'
    return word.title() if not set(word).difference(letters) else False

sentence = input('Введите строку из слов, разделенных пробелами: ').split()
for el in sentence:
    result = int_func(el)
    if result:
        print(int_func(el), end=' ')
