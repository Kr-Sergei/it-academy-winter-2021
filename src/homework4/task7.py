# Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи
# алгоритма Евклида (мы не знаем функции и рекурсию).


a = 462
b = 1071

if a > b:
    while b > 0:
        n = a % b
        a, b = b, n
    print(a)
elif a < b:
    while a > 0:
        n = b % a
        b, a = a, n
    print(b)
elif a == b:
    print(a)
