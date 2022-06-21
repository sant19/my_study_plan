number = int(input("Enter a number: "))

cont = 0
for i in range(2, number - 1):

    if (number % i) == 0:
        cont = 1


if cont == 1:
    print("Not a Prime Number")
else:
    print("Prime Number")
