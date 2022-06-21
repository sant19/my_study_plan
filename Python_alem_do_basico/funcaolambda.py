# Função regular
def double(n):
    return n * 2


print(double(10))


# usando lambda
double = lambda n: n * 2
print(double(10))


# Multiplos argumentos no lambda
"""Programa para clacular o produto de 2 números"""
product = lambda x, y: x * y


result = product(5, 10)
print(result)
