def print_items(*numbers):
    for number in numbers:
        print(number)


text1 = input("Enter text1: ")
text2 = input("Enter text2: ")
print_items(text1)
print_items(text1, text2)
