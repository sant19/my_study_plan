total_friends = int(input("Enter friends number: "))
total_bill = int(input("Enter value bill: "))


subtotal = total_bill + (total_bill * 0.20)
total = subtotal / total_friends
print(total)
