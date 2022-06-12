principal = float(input("Enter principal value: "))
rate = float(input("Enter a rate: "))
time = float(input("Enter time: "))


interest = principal * rate * time * 0.01
total_sum = principal + interest


print(interest)
print(total_sum)
