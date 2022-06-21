n = int(input("Enter a number: "))
t1 = 1
t2 = 1
result = 0

for i in range(1, n + 1):
    print(t1)
    result = t1 + t2
    t1 = t2
    t2 = result
