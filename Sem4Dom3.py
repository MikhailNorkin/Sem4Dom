#3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
#Пример:
#Волков Андрей 5
#Наталья Тарасова 5
#Фредди Меркури 3
#Денис Байцуров 4

#Программа выдаст:
#ВОЛКОВ АНДРЕЙ 5
#НАТАЛЬЯ ТАРАСОВА 5
#Фредди Меркури 3
#Денис Байцуров 4


def turn_to_int(element):
    if element.isdigit():
        return int(element)
    return element

with open('text.txt', encoding='utf-8') as file:
    names_with_marks = file.read().split('\n')
    file.close()

    with open('text.txt', 'r+', encoding='utf-8') as file:
        for i,record in enumerate(names_with_marks):
            record = record.rsplit(' ',maxsplit=1)
            names_with_marks[i] = list(map(turn_to_int,record))
            if names_with_marks[i][-1]>4:
                file.write(names_with_marks[i][0].upper() + " " + str(names_with_marks[i][-1])+"\n")
            else:
                file.write(names_with_marks[i][0] + " " + str(names_with_marks[i][-1])+"\n")    
    file.close()        
print("Готово! Файл text.txt изменен!")