def count(list):
    count_dict ={}
    for item in list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_Str = input("Enter list(split by ' '):")
word_list = input_Str.split()
count_dict = count(word_list)
print("Count of each word in given list: ",count_dict)