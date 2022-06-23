try:
    numbers = [10, 20, 30]
    index = int(input("Enter index: "))

    print(numbers[index])
    if numbers[index] not in numbers:
        print('Index is wrong')
except IndexError:
    print("Index is wrong")
