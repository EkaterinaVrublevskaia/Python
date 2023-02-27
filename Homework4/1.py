# 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах. Если таких чисел нет - выдать
# внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

box_1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
box_2 = [3, 6, 9, 12, 15, 18]

set_box_1 = set(box_1)
set_box_2 = set(box_2)
print(set_box_1)
print(set_box_2)  


for i in set_box_1:
    print(i, end = ' ') if i in set_box_2 else (i, 'Повторяющихся чисел нет!')

try:
    for i in set_box_1:
        for j in set_box_2:
            if i == j:
                print(i, end = ' ')
except:
    print("Повторяющихся чисел нет!")



# не верно работает с else, все проверяет. 
# for i in set_box_1:
    # for j in set_box_2:
    #     if i == j:
    #         print(i, end = ' ')
    #         break
    #     else:
    #         print("Повторяющихся чисел нет!") 

# try:
#     for i in set_box_1:
#         for j in set_box_2:
#             if i == j:
#                 print(i, end = ' ')
# except:
#     print("Повторяющихся чисел нет!")




# 
# set_box = set_box_1.intersection(set_box_2)
# list_box = list(set_box)
# for i in range(len(list_box)):
#     print(list_box[i], end = ' ')
        



       

           