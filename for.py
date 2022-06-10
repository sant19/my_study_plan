"""
Usado para iterar sobre uma sequência, como strings ou um intervalo de números
"""

name = "Eva"

for item in name:
    print(item)

""" Usando for loop com listas """
languages = ['English', 'German', 'french']

for language in languages:
    print('Language is', language)


""" Usando for loop com range """
for item in range(1, 5):
    print(item)


for item in range(2, 4):
    result = item + 1
    print(result)


""" Imprimir caracteres individuais """
caracteres = input('Enter caracter: ')

for caracter in caracteres:
    print(caracter)


""" Soma de números naturais """
n = int(input("Enter a positive number: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Result:", total)


""" Fatorial de um número """
num = int(input("Enter a number: "))
total = 1

for i in range(1, num + 1):
    total = total * i
print(total)

""" Usando a instrução if dentro de um loop """
for number in range(1, 10):
    if number % 2 == 0:
        print(number)


""" Imrpimir números ímpares """
n = int(input("Enter a number: "))

for numero in range(1, n + 1):
    if numero % 2 != 0:
        print(numero)
