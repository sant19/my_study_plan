number = int(input("Ente a number: "))


for i in range(1, number + 1):
    if number % i == 0:
        print(i)
