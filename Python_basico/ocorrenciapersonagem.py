string1 = input("Enter a estring: ")
caracter1 = input("Enter a caracter: ")


count = 0
for i in string1:
    if caracter1 in i:
        count = count + 1
print(count)
