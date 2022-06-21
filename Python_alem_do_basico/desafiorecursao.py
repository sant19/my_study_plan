def calcular_fatorial(n):

    if n != 1:
        return n * calcular_fatorial(n - 1)

    return n


number = int(input("Enter a positive number: "))
result = calcular_fatorial(number)
print(result)
