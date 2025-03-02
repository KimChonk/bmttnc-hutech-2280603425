def reverse_list(list):
    return list[::-1]

input_list = input("Enter list(split by ','):")
numb = list(map(int,input_list.split(',')))
reversed_list = reverse_list(numb)
print("List after reversed : ",reversed_list)