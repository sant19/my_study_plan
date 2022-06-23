class Person:
    def __init__(self):
        person_name = input("Enter name: ")
        person_age = input("Enter age: ")
        self.name = person_name
        self.age = person_age

    def display_info(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')


person1 = Person()
person1.display_info()


person2 = Person()
person2.display_info()
