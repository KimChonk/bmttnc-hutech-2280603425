def truy_cap(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
input_tuple = eval(input("Enter tuple(example : (1,2,3) ):"))
first,last = truy_cap(input_tuple)
print("First element of tuple: ",first)
print("Last element of tuple: ",last)