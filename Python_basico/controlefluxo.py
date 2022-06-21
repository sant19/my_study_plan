age = int(input("Enter age: "))

if age >= 18:
    print("The person can vote.")
else:
    print("The person cannot vote.")


# Negativo ou Positivo
number = int(input("Enter number: "))

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")


# Par/Ímpar
number1 = int(input("Enter number: "))

if number1 % 2 == 0:
    print("even")
else:
    print("odd")
