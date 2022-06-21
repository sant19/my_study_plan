Marks = int(input("Enter marks: "))


if Marks < 0 or Marks > 100:
    print("Invalid Marks")
elif Marks > 40:
    print("Pass")
else:
    print("Fail")
