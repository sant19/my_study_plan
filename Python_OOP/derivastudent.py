class Person:
    def __init__(self):
        person_name = input("Enter name: ")
        person_age = input("Enter age: ")
        self.name = person_name
        self.age = person_age

    def display_info(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')


class Student(Person):
    def __init__(self, student_id):
        self.id = student_id
        super().__init__()

    def display_info(self):
        super().display_info()
        print(f'id: {self.id}')


student1 = Student(12)
student1.display_info()
