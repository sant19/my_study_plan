def find_sum(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma


number = int(input("Enter a number: "))
result = find_sum(number)
print(result)
