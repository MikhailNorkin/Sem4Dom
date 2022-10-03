# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

import SemLib as name

number = name.get_number(f"Введите количество элементов: ")

list_of_numbers = []
list_of_numbers_all = []
for i in range(number):
    next_number = name.get_number(f"Введите {i+1} элемент: ")
    list_of_numbers_all.append(next_number)
    flag = True
    for j in list_of_numbers:
        if next_number == j:
            flag = False
            break
    if flag == True:
        list_of_numbers.append(next_number)
print(list_of_numbers_all,' -> ',list_of_numbers)        
