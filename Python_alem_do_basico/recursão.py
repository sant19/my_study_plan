# Uma função que chama a si mesma é chamada recursiva (recursão


# Exemplo de recursão simples
def print_variable():
    text = 'Hello'
    print(text)

    # Chama print_variable dentro da própria função
    print_variable()


print_variable()


# Exemplo recursão infinita
def print_number(n):
    print(n)
    print_number(n + 1)


print_number(1)


# Exemplo de recursão finita
def calculate_sum(n):

    if n != 0:
        n = n + calculate_sum(n - 1)
    return n


result = calculate_sum(3)
print(result)
