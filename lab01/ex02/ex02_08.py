def chia_het_5(binary):
    decimal = int(binary, 2)
    if decimal % 5 == 0:
        return True
    else:
        return False
binary_Str = input("Enter a binary number (plit by ',' ): ")
binary_List = binary_Str.split(',')
so_chia_het_5 = [num for num in binary_List if chia_het_5(num)]
if len(so_chia_het_5) == 0:
    print("No number is divisible by 5")
else:
    print("Numbers divisible by 5 are: ", ' '.join(so_chia_het_5))