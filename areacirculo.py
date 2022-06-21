def compute_area(radius, pi):
    area = pi * radius * radius
    return area


radius = float(input("Enter radius: "))
pi = 3.14
result = compute_area(radius, pi)
print(result)
