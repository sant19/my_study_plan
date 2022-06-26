# Exemplo adicionar números
def multiply_numbers(*numbers):
    # Calcular o produto de um tupla
    total = 1
    for number in numbers:
        total = total * number
    return total


n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))


# Chama multiply_numbers com 3 argumentos
result = multiply_numbers(n1, n2, n3)
print(result)
