'''
Ввод целого числа
'''
def get_number(input_string):
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print("Вы не ввели число!")