# Argumentos posicionais
def display_info(name, age):
    print(name)
    print(age)


display_info('Amanda', 22)


# Argumentos de palavra_chave
def display_info(name, age):
    print(f'name = {name}')
    print(f'age = {age}')


display_info(age='22', name='Amanda')


# Argumentos padrão
def greet(massage='Howdy'):
    print(massage)


greet()


# Exemplo argumento padrão
def display(symbol='*', number=5):
    print(f'symbol = {symbol}')
    print(f'number = {number}')


print('Quando os argumentos não são passados.')
display()

print('Quando o 1º argumento é passado.')
display('#')

print('Quando ambos argumentos saõ passados.')
display('$', 5)


# Argumentos padrão em print()
print('Hello', 'there')
print('Hello', 'there', sep='###')


# Argumento variável
def greet(*mensages):
    print(mensages)


# Chamando greet() com 1 argumento
greet('Hi')

# Chamando greet() com 2 argumentos
greet('Hi', 'Hello')

# Chamando greet() sem nenhum argumento
greet()


# Exemplo adicionar números
def add_numbers(*numbers):
    # Calcular a soma de um tupla
    total = 0
    for number in numbers:
        total = total + number
    return total


# Chama add_numbers com 2 argumentos
result = add_numbers(5, 10)
print(result)

# Chama add_numbers com 3 argumentos
result = add_numbers(5, 10, 20)
print(result)
