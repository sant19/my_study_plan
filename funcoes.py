def print_numbers():
    print(5)
    print(100)


print_numbers()
print_numbers()


# Argumentos da função
def greet(name):
    print('Hello', name)
    print('How do you do?')


greet('Emma')


def plus_ten(number):
    result = number + 5
    print(result)


plus_ten(100)
plus_ten(20)


# Passando vários argumentos
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)


number1 = 5
number2 = 6
add_numbers(number1, number2)


def display_info(name, location):
    print(name)
    print(location)


country = input('Enter Country: ')
display_info("Taylor", country)


def get_product(number1, number2):
    result = number1 * number2
    return result


n1 = int(input('Enter Number1: '))
n2 = int(input('Enter Number2: '))
total = get_product(n1, n2)
print(total)
