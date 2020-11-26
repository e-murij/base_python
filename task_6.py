result_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        sudject = line.split()
        sum = 0
        for el in sudject[1:]:
            str = '0'
            i = 0
            while el[i].isdigit():
                str = str + el[i]
                i += 1
            sum = sum + int(str)
        result_dict[sudject[0][0:len(sudject[0]) - 1]] = sum
print(result_dict)
