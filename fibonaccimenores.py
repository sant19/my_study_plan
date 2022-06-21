n = int(input("Enter a number: "))
t1 = 1
t2 = 1
result = 0


while t1 < n:
    print(t1)
    result = t1 + t2
    t1 = t2
    t2 = result
