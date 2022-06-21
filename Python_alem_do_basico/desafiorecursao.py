def calcular_fatorial(n):
    """

    Calcula a Fatorial de um número

    """

    if n != 1:
        return n * calcular_fatorial(n - 1)

    return n


number = int(input("Enter a positive number: "))
result = calcular_fatorial(number)
print(result)
