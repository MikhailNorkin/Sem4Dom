eng_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def sifr_ceasar(string:str, k:int):

    string_sifr =''
    for s in string:
        if s.isalpha() and s in eng_alph:
            print(s)    
            index = eng_alph.find(s) + k
            if index > 51:
                index += -52
                string_sufr += eng_alph[index]
            else:
                string_sifr += eng_alph[index]
        else: 
            string_sifr += s        
    return string_sifr

def write_file(string:str, num: int):
    with open('text2.txt', 'w', encoding="utf-8") as f:
        f.write(sifr_ceasar(string, num))

def read_file(num:int):
    with open('text2.txt', 'r', encoding="utf-8") as f:
        string_fail = f.read()
        print('Зашифрованная фраза:\n', string_fail)
        print()
        print('Дешифрованная фраза:\n', sifr_ceasar(string_fail, num))

number = int(input('Введите ключ шифрования: '))
string_input = 'bin'
name_fail = 'Task2.txt'
write_file(string_input,  number)
read_file(- number)