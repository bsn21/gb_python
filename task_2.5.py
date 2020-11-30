# Реализовать структуру «Рейтинг»,
# представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

rating = [7, 3, 3, 2]

while True:
    user_num = int(input('\nВведите число: '))
    min_num, max_num = min(rating), max(rating)

    if user_num in rating:
        idx = rating.index(user_num) + 1
        rating.insert(idx, user_num)
    elif user_num > max_num:
        rating.insert(0, user_num)
    elif user_num < min_num:
        rating.append(user_num)
    else:
        for i in range(len(rating)):
            if rating[i] < user_num:
                rating.insert(i, user_num)
                break
        # # можно написать как в коментарии ниже, но лучше, наверное, 1 вариант
        # # 2 вариант:
        # for i in rating:
        #     if i < user_num:
        #         rating.insert(rating.index(i), user_num)
        #         break
    print(rating)