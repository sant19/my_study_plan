class Animal:
    def eat(self):
        print("I can eat")


# Classe dog derivada da classe animal
class Dog(Animal):
    def bark(self):
        print("I can bark")


class Cat(Animal):
    def get_grumoy(self):
        print("I am getting grumpy")


# Objeto da classe dog
dog1 = Dog()


# Chama o método bark() (de Dog)
dog1.bark()


# Chama o método eat() (de Animal)
dog1.eat()


# Objeto de Cat
cat1 = Cat()
cat1.eat()


# Exemplo de herança Python
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with strainght lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges.")


t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)
t1.display_info()


p1 = Polygon([2, 4, 5])
p1.display_info()
perimeter = p1.get_perimeter()
print(f'Perimeter: {perimeter}')


# Usando super()
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines.")


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges.")

        # Chama o método display_info() do Polygon
        super().display_info()


t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)
t1.display_info()
