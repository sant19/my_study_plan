"""
    A programação orientada a objetos (POO) é uma técnica popular para
    resolver problemas de programação criando objetos.
"""


# Classes e objetos
'''Há duas etapas envolvidas na criação de objetos'''

'''
    1. Definir uma classe
    2. Criar objetos da classe
'''

# Definir uma classe


# Criando uma classe
class Student:
    pass


# Fora da classe
# Criando objetos para student
student1 = Student()
student2 = Student()


# Adicionando atributos
class Student:
    pass


# Cria objetos
student1 = Student()


# Adiciona atributos
student1.name = 'Harry'
student1.score = 85


# Imprimir atributos de student1
print(student1.name)
print(student1.score)


# Adicionando métodos
class Student:

    # Adiciona um método para verificar a aprovação/reprovação
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False


# Cria os objetos
student1 = Student()


# Adiciona atributos
student1.name = 'Harry'
student1.score = 85


# Chama o método check_pass_fail()
# Chamando esse método usando objeto student1
did_pass = student1.check_pass_fail()
print(did_pass)


class Student:
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False


student1 = Student()
student1.name = 'Harry'
student1.score = 85


did_pass = student1.check_pass_fail()
print(f'Did {student1.name} pass?', did_pass)


student2 = Student()
student2.name = 'Ronin'
student2.score = 35


did_pass = student2.check_pass_fail()
print(f'Did {student2.name} pass?', did_pass)


# Adicionando atributos de maneira adequada
class Test:
    def __init__(self):
        print('Hello there')


test1 = Test()
test2 = Test()


# Adicionando o método __init__
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


# Adicona um método para checar aprovado/reprovado
def check_pass_fail(self):
    if self.score >= 40:
        return True
    else:
        return False


# Cria objeto
student1 = Student('Harry', 85)


did_pass = student1.check_pass_fail()
print(f'Did {student1.name} pass', did_pass)


student2 = Student('Ronin', 35)


did_pass = student2.check_pass_fail()
print(f'Did {student2.name} pass', did_pass)


# Lembre-se disso
# Lembre-se dessa estrutura para adicionar atributos
class Test:
    def __init__(self, attr1, attr2):
        self.attribute_name1 = attr1
        self.attribute_name2 = attr2


# Cria um objeto
test1 = Test(10, 20)
print(test1.attribute_name1)
print(test2.attribute_name2)


# Cria um objeto
test2 = Test(100, 200)
print(test2.attribute_name1)
print(test2.attribute_name2)


# Usando Objetos como argumentos
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Cria um objeto
person1 = Person('Ana', 21)
print(person1.name)
print(person1.age)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person_attributes(self, person):
        print(self.name)
        print(self.age)
        print(person.name)
        print(person.age)


person1 = Person('Ana', 21)
person2 = Person('Sara', 20)
person1.print_person_attributes(person2)


# Retornando Objetos de Métodos
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def return_another_person(self):
        person = Person('Sara', 20)
        return person


person1 = Person('Ana', 21)


another_person = person1.return_another_person()
print(another_person.name)
print(another_person.age)


# Exemplo adicionar números
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imaginary = imag

    def add(self, number):
        result_real = self.real + number.real
        result_imaginary = self.imaginary + number.imaginary

        result = Complex(result_real, result_imaginary)
        return result


n1 = Complex(5, 6)
n2 = Complex(-4, 2)


n3 = n1.add(n2)


print('real part =', n3.real)
print('imaginary part =', n3.imaginary)
