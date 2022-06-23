my_dict = dict()

for i in range(1, 3 + 1):
    key = input("Enter Key: ")
    value = input("Enter Value: ")
    i = {key, value}
    my_dict.update([i])


print(my_dict)
