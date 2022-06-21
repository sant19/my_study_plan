def check_prime(number):
    flag = 0
    for i in range(2, number - 1):
        if number % i == 0:
            flag = 1
    flag += 1

    if flag == 1:
        print("Prime Number")
    else:
        print("Not a Prime Number")


number = int(input("Number a number: "))
check_prime(number)
