import math


number = int(input("Enter a number: "))
square_root = math.sqrt(number)
check_remainder = square_root % 1


if check_remainder == 0:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
