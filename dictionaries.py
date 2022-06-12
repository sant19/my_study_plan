"""
    Um dicionário é uma coleção de itens, semelhantes a listas e tuplas.
    No entanto, cada item do dicionário é um par chave/valor .
"""


person = {'name': 'Angela', 'age': 20}
print(person)


"""
    O importante a ser lembrado sobre dicionários é que as chaves 
    de um dicionário devem ser objetos únicos e imutáveis 
    ​​(que não podem ser alterados).
"""

dict1 = {}
dict2 = {1: 'one'}


# Acesso aos Valores do dicionário
student_info = {
    'name': 'Kyle',
    'major': 'computer Science',
    'age': 19
}


print(student_info['name'])
print(student_info['age'])


# Atualizar valor de uma chave
student_info = {
    'name': 'Kyle',
    'major': 'CS',
    'age': 19
}
# changing the value of the 'age' key to 20
student_info['age'] = 20
# changing the value of the 'name' key to 'Mike'
student_info['name'] = 'Mike'
print(student_info)


# Adicionar Item
student_info = {
    'name': 'Kyle',
    'major': 'CS',
}
# If we assign a value to the key that doesn't exist,
# it is added to the dictionary 
student_info['city'] = 'London'
print(student_info)


prices = {
    'apple': 2.5,
    'kiwi': 3.4
}

prices['apple'] = 3.5
print(prices)


prices['banana'] = 3
print(prices)


# Excluir item do dicionário
student_info = {
    'name': 'Kyle',
    'major': 'CS',
}
# deleting the item
del student_info['name']
print(student_info)

# Exclui todo o dicionário
student_info = {
    'name': 'Kyle',
    'major': 'CS',
}
# deleting the dictionary
del student_info
print(student_info)


# Iterando por meio de um dicionário
squares = {1: 1, 3: 9, 5: 25}
for key in squares:
    print(key)


squares = {1: 1, 3: 9, 5: 25}
for key in squares:
    
    # getting the value of a key
    value = squares[key]
    print(f'{key} -> {value}')


prices = {'apple': 2, 'kiwi': 3}

for key in prices:
    value = prices[key]
    print(f'{value}')


# Métodos de dicionário

"""O método get()"""
scores = {'Physics':67, 'Maths':87}


print(scores.get('Physics'))
print(scores.get('Maths')))


"""O método clear()"""
# remove todos os itens de um dicionário.
scores.clear()


"""O método copy()""""
original_marks = {'Physics':67, 'Maths':87}
copied_marks = original_marks.copy()
print(f'Original Marks: {original_marks}')
print(f'Copied Marks: {copied_marks}')


