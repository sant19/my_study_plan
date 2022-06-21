def greet(**kwargs):
    print(kwargs)


formal = input("Enter formal: ")
informal = input("Enter informal: ")
greet(formal=formal, informal=informal)
