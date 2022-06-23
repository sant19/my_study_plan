# Alguns tipos de exceções:


'''Exceção IndexError'''
numbers = [2, 8, 5]
# Não existe o index 4
print(numbers[4])


'''Exceção KeyError'''
person = {'name': 'Stuart', 'age': 30}
# Não existe a chave profession
print(person['profession'])


'''Exceção valueError'''
import math


# sqrt atribuido a uma string
result = math.sqrt('Hello')
print(result)


# Tratamento de exceções
try:
    # Código que pode causar exceção
except:
    # Código para rodar quando a exceção ocorrer


try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator/denominator
    
    print(result)
except:
    print("Denomiador não pode ser 0. Tente novamente")


# Exemplo tratamento de exceções específica
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    
    result = numerator/denominator
    print(result)
    
    my_list = [1, 2, 3]
    index = int(input("Enter index: "))
    
    print(my_list[index])

except ZeroDivisionError:
    print("Denominador não pode ser 0. Tente novamente")

except IndexError:
    print("Index está errado")


# Lindando com várias exceções
try:
    result = 5/0
    print(result)

    my_list = [1, 2, 3]
    print(my_list[20])

except ZeroDivisionError:
    print("Denominador não pode ser 0")

except IndexError:
    print("Index não existe")
