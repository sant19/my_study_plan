# Acessar itens de tupla
languages = ('Python', 'JavaScript', 'C++')
# access first item
first_language = languages[0]
print(first_language)
# access second item
print(languages[1])
# access third last item
print(languages[-3])


odd_numbers = (9, 11, 15, 17)

print(odd_numbers[2])

""" Tuplas são imutáveis """

""" Não podemos excluir itens individuais de uma tupla. """

""" No entanto, é possível excluir a própria tupla. """
animals = ('dog', 'cat', 'rat')
# deleting the tuple
del animals


# Iterar por meio de uma tupla
fruits = ('apple', 'banana', 'mango')
for fruit in fruits:
    print("I like", fruit)


movie = 'Snowpiercer'

print(movie[3])


# Métodos de string

"""replace()"""
"""O método find()"""
"""Os métodos upper() e lower()"""


text1 = input('')
text2 = input('')


result = text1[:4] + text2[-4:]
print(result)
