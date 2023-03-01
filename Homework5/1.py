# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. 
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

def step_number(a, b):
    if b == 0:
        return 1
    else:
        return a * step_number(a, b - 1)

print(step_number(a, b))
print(step_number(2, 3))