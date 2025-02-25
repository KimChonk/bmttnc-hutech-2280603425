def total(list):
    total = 0
    for num in list:
        if num % 2 == 0:
            total += num
    return total
input_list = input("Enter list(split by ','):")
numb = list(map(int,input_list.split(',')))
total_num = total(numb)
print("number of sochan in given list:",total_num)
