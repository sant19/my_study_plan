numbers = [1, 2, 3, 4]


# Criando um dicionário vazio
square_numbers = {}


# Usando um  loop para adicionar itens ao dicionário
for number in numbers:
    square_numbers[number] = number ** 2


print(square_numbers)


# Exemplo Dictionary comprehension
numbers = [1, 2, 3, 4]


square_numbers = {number: number ** 2 for number in  numbers}
print(square_numbers)


# Exemplo Dictionary comprehension com condições
numbers = [1, 2, 3, 4]

square_numbers = {number: number ** 2 for number in numbers if number > 2}
print(square_numbers)
