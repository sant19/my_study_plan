# Introdução aos conjuntos


"""
Semelhante a listas e tuplas, um conjunto é uma coleção de itens. 
Há três coisas que diferenciam os conjuntos de listas e tuplas:

* não ordenados - os itens de um conjunto não estão em nenhuma ordem específica
* único - um conjunto não pode conter itens duplicados
* itens imutáveis ​​- os itens devem ser imutáveis
"""

"""
Criando conjuntos
Um conjunto é criado colocando itens dentro de chaves { }, 
separados por vírgulas. Por exemplo,
"""

animals = {'dog', 'cat', 'tiger'}
print(animals)
mixed_set = {4, 'tiger', 3.5}
print(mixed_set)


# Criando um conjunto vazio
my_set = set()
print(my_set)


# Adicionar itens de conjunto
numbers = {1, 3}
print(numbers)
# add an item
numbers.add(2)
print(numbers)


# Atualizar conjunto
animals = {'dog', 'cat'}
wild_animals = ['tiger', 'lion', 'lion']
animals.update(wild_animals)
print(animals)


numbers = set()


number = int(input('Enter a number: '))
numbers.add(number)
print(numbers)


# Remover item de um conjunto
"""
Usamos o discard()método para remover o item especificado do conjunto.
"""

animals = {'tiger', 'cat', 'dog'}
# Remove the 'cat' item
animals.discard('cat')
print(animals)


# Operadores de conjunto
"""
|operador.
"""

domestic_animals = {'dog', 'cat', 'elephant'}
wild_animals = {'lion', 'tiger', 'elephant'}
# union of sets
animals = domestic_animals | wild_animals
print(animals)


# Conjuntos de interseção
"""
&operador.
"""
domestic_animals = {'dog', 'cat', 'elephant'}
wild_animals = {'lion', 'tiger', 'elephant'}
# intersection of sets
animals = domestic_animals&  wild_animals
print(animals)


# CONVERTER TIPO DE DADO

"""
* list()- converte para lista
* tuple()- converte para tupla
* dict()- converte para dicionário
* set()- converte para definir
"""

# convert tuple to list
result = list((1, 2, 3))   # [1, 2, 3]
print(result)
# convert string to list
result = list('Hello')   # ['H', 'e', 'l', 'l', 'o']
print(result)
# convert dictionary to list
result = list({2: 4, 10: 20})   # [2, 10]
print(result)
# convert set to list
result = list({1, 2, 3})   # [1, 2, 3]
print(result)


result = tuple([1, 2, 3])   # (1, 2, 3)
print(result)
# convert string to tuple
result = tuple('Hello')   # ('H', 'e', 'l', 'l', 'o')
print(result)
# convert dictionary to tuple
# dictionary's keys will be tuple's items
result = tuple({2: 4, 10: 20})   # (2, 10)
print(result)
# convert set to tuple
result = tuple({1, 2, 3})   # (1, 2, 3)
print(result)


# convert to dictionary
coordinate = dict([('x', 5), ('y', -5)])
print(coordinate)   # {'x': 5, 'y': -5}
# convert to dictionary
coordinate = dict(x = 5, y = -5)
print(coordinate)   # {'x': 5, 'y': -5}


# convert list to set
result = set([1, 2, 3])
print(result) # {1, 2, 3}
#convert string to set
result = set('abca')
print(result) # {'a', 'b', 'c'}
# convert tuple to set
result = set((1, 2, 3, 2, 3))
print(result) # {1, 2, 3}
# convert dictionary to set
result = set({2: 4, 10: 20}) # (2, 10)
print(result)


# Remover itens duplicados de uma lista
numbers = [1, 1, 2, 3, 4, 1, 1]
numbers = list(set(numbers))
print(numbers)


numbers = range(4, 11, 3)
result = tuple(numbers)
print(result)


