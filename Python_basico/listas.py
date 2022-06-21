odd_numbers = [9, 11, 15]
print(odd_numbers[1])


# Excluir itens de uma lista
animals = ['dog', 'cat', 'rat']
# deleting the second item
del animals[1]
print(animals)
# delete the first item
del animals[0]
print(animals)


# excluir a lista inteira.
animals = ['dog', 'cat', 'rat']
# deleting the list
del animals


# Listar métodos

"""O método append()"""
animals = ['dog', 'cat']
# adding 'rabbit' at the end of the list
animals.append('rabbit')
print(animals)

"""O método extend()"""
animals = ['dog', 'cat']
animals1 = ['rabbit', 'pig']
# adding items of animals1 list to the animals list
animals.extend(animals1)
print(animals)

"""O método insert()"""
animals = ['dog', 'cat', 'rat']
# 'rabbit' is inserted at the third position (index 2)
animals.insert(2, 'rabbit')
print(animals)

"""O método copy()"""
animals1 = ['dog', 'cat', 'rat']
animals2 = animals1.copy()
print(animals2)
# Output:
['dog', 'cat', 'rat']


animals = []

animals.append('dog')
print(animals)

animals.append('cat')
print(animals)


# Iterar através de uma lista
fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print("I like", fruit)


# Verificação de associação
fruits = ['apple', 'banana', 'mango']
if 'apple' in fruits:
    print('apple is tasty')
if 'potato' in fruits:
    print('Whaaaat?')


numbers = [10, 20, 30, 40]

comprimento = len(numbers)
print(comprimento)
