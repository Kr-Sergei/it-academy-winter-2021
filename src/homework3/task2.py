# List practice
# 1. Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# 2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
# 3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
# 4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# 5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке
# этого элемента не было.


lst1 = [(elem1 + elem2) for elem1 in 'ab' for elem2 in 'bcd']
print(lst1)

lst2 = lst1[::2]
print(lst2)

lst3 = [(str(elem1) + 'a') for elem1 in '1234']
print(lst3)

print(lst3.pop(1))

lst5 = lst3.copy()
lst5.insert(1, '2a')
print(lst3)
print(lst5)
