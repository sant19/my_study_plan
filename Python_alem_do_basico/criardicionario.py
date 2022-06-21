n = int(input("Enter the number: "))


numbers = {n: n * 10 for n in range(1, n + 1) if n >= 3}
print(numbers)
