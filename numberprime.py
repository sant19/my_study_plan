number = int(input("Enter a number: "))


is_prime = True


for i in range(2, number):
    if (number % i) == 0:
        is_prime = False
        break


if is_prime:
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')


# Criando uma função
def check_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True


number = int(input("Enter a number: "))


is_prime = check_prime(number)


if is_prime:
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')


# Números primos entre 50 e 100
def check_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
n1 = 50
n2 = 100
# iterating loop from 50 to 100
for number in range(n1, n2+1):
    is_prime = check_prime(number)
    # printing if number is prime
    if is_prime:
        print(number)