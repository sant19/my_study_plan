# Maneira analítica de fazer
numbers = []


for i in range(1, 6):
    numbers.append(2 ** i)


print(numbers)


# Forma concisa de fazer
numbers = [2 ** i for i in range(1, 6)]
print(numbers)


# Também pode ser feira com If
numbers = [12, 15, 21, 32, 14]
even_numbers = [n for n in numbers]
print(even_numbers)


# Para obter apenas números pares
numbers = [12, 15, 21, 32, 14]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
