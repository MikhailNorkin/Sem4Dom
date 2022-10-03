# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import Sem4Dom4.SemLib as name

number = name.get_number(f"Введите натуральное число: ")

list_of_numbers = []
for i in range(2, number):
    if number % i == 0: #провека, что число делится на введенное
        flag = True
        for j in range(2,i): #проверим, что число простое
            if i % j == 0:
                flag = False
                break
        if flag == True:
            list_of_numbers.append(i)
print('Список всех простых множителей числа', number,':',list_of_numbers )

