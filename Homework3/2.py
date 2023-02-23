# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. Пользователь вводит 
# это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

number_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = int(input("Введите число x: "))
result = 0
for i in number_list:
    if x != i:
        number_list.append(x)
        number_list.sort()
        temp = number_list.index(x) + 1
        result = number_list[temp]  
        break          
    else:
        result = i 
        break
    
print(result)