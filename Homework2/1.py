# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет,которые нужно перевернуть. Количество монет
# и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2
import random

n = int(input("Введите количество монет, которые лежат на столе: "))
list = []
k = 0
for i in range(n):
    list.append(random.randint(0, 1))
    if list[i] == 1:
        k += 1
print(list)
print(k if k < n / 2 else n - k)

    