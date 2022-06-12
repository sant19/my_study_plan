"""
    Qualquer variável criada dentro de uma função é local para ela
"""


def add_numbers(n1, n2):
    # Variável local
    result = n1 + n2
    return result


output = add_numbers(2, 5)
print(output)


''' As variáveis ​​locais são importantes porque tornam as funções
    independentes.
'''


""" podemos usar essa função se soubermos duas coisas:

* argumentos que a função recebe
* valor de retorno da função
"""


def add_numbers(n1, n2):
    result = n1 + n2
    return result


n1 = 2
n2 = 5
result = add_numbers(n1, n2)
print(result)


# Soma de números naturais de 1 a n
def compute_sum(number):
    total = 0

    for i in range(1, number + 1):
        total = total + 1
    return total


total = compute_sum(10)
print(total)


# Fatorial de um número
def compute_factorial(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


number = int(input('Enter number: '))
total = compute_factorial(number)
print(total)


# Maior número entre três números
def get_largest_number(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


largest_number = get_largest_number(3, 55, -5)
print(largest_number)


# Verificar Ímpar/Par
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


n = int(input("Enter an integer: "))


result = is_even(n)
if result:
    print(n, 'is even')
else:
    print(n, 'is odd')


# Obter pontuação média
def get_average_score(scores):
    total = sum(scores)
    count = len(scores)

    average_score = total / count
    return average_score


scores = [55, 64, 75, 80, 65]
average_score = get_average_score(scores)
print(average_score)


# Calcular a nota do aluno
def compute_grade(average_score):
    if average_score >= 80.0:
        grade = 'A'
    elif average_score >= 60.0:
        grade = 'B'
    elif average_score >= 50.0:
        grade = 'C'
    else:
        grade = 'F'
    return grade


average_score = 67.8


grade = compute_grade(average_score)
print(grade)
