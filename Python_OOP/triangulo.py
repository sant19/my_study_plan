class Triangle:
    def __init__(self, a, b, c):
        self.lado_a = a
        self.lado_b = b
        self.lado_c = c

    def get_perimeter(self):
        perimeter = self.lado_a + self.lado_b + self.lado_c
        return perimeter


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


triangle = Triangle(a, b, c)
result = triangle.get_perimeter()
print(result)


# Tudo é um objeto
# Função type()
number = 10
print(type(number))


numbers = [1, 4, 9, 16]
print(type(numbers))

flag = True
print(type(flag))


def my_function():
    pass


print(type(my_function))


# Função dir()
'''Lista todos os atributos e métodos do objeto fornecido'''
number = 1
print(dir(number))

# método __add__()
number = 5
result = number.__add__(100)
print(result)
# resultado 105


# Função id()
number1 = 5
print(id(number1))


number2 = 10
print(id(number2))


number1 = 5
print(id(number1))

number2 = number1
print(id(number2))


# método copy()
list1 = [1, 2, 3]

list2 = list1.copy()

list1.append(4)

print(list1)
print(list2)
