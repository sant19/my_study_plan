my_dict = {"a": "juice", "b": "grill", "c": "corn"}


data = input("Enter a data: ")
flag = False

for i in my_dict.values():
    if data in i:
        flag = True
        break


if flag is True:
    print("Value found")
else:
    print("Value not found")
