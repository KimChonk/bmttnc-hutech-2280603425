def delete(dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dict = {'a':1,'b':2,'c':3,'d':4,'e':5}
print("Dictionary before deletion:",my_dict)
key = input("Enter key to delete:")
is_deleted = delete(my_dict,key)
if is_deleted:
    print("Key is deleted successfully")
    print("Dictionary after deletion:",my_dict)
else:
    print("Key is not present in dictionary")