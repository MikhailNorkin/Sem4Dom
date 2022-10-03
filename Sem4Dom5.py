data_file = 'AAAAAAFDDCCCCCCCCCCAEEEEEEEEEE'
file_1 = open("Text3.txt", "w")
file_2 = open("Text4.txt", "w")

def compression(data):
    encoding = ''
    prev_char = ''
    count = ''
    if not data:
        return ''
    for i in data:
        if i != prev_char:
            encoding += str(count) + prev_char
            count = 1
            prev_char = i
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def recovery(data):
    decode = ''
    count = ''
    for i in data:
        if i in data:
            count += i
        else:
            decode += i * int(count)
            count =''
    return decode

file_1.write(recovery((data_file)))            
file_2.write(compression(data_file))
file_1.close()
file_2.close()


