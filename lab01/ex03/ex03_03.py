def create_tuple_from_list(list):
    return tuple(list)
input_list = input("Enter list(split by ','):")
numb = list(map(int,input_list.split(',')))
tuple_num = create_tuple_from_list(numb)
print("List: ",numb)
print("Tuple from list : ",tuple_num)