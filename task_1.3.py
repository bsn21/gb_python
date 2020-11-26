# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = input('Введите число n: ')

nn = n + n
nnn = nn + n
result = int(n) + int(nn) + int(nnn)

print(f'n + nn + nnn = {result}')
