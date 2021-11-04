

# 123 .... 10 11 12

input_user = float(input('input value less than 3 or greather than 10 : \n'))

is_kurang_dari_3 = input_user < 3
print(is_kurang_dari_3)

is_lebih_dari_10 = input_user > 10
print(is_lebih_dari_10)

is_valid_or = is_kurang_dari_3 or is_lebih_dari_10
print(is_valid_or)


#union
#...... 456789 .....
print("\n", 20*"=", "\n")
input_user = float(input('input value in range > 3 and < 10 : \n'))

is_lebih_dari3 = input_user > 3
print(is_lebih_dari3)

is_kurang_dari10 = input_user < 10
print(is_kurang_dari10)

is_valid_and = is_lebih_dari3  and is_kurang_dari10
print(is_valid_and)