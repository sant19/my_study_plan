"""
break -> termina o loop imediatamente quando é encontrada
continue -> permite pular instruções dentro do loop
"""

for i in range(1, 6):
    print(i)
    break
print("This is outside the loop")

for i in range(1, 6):
    print(i)
    if i == 3:
        break
print("This is outside the loop")


total = 0

while True:
    n = float(input('Enter a number: '))

    if n == 0:
        break
    total = total + n

print("Result:", total)


total = 0

while True:
    num = int(input('Enter a number: '))
    if num == 0 or num < 0:
        break
    total = total + num
print(total)


# CONTINUE
for number in range(1, 11):
    # condition to check odd number
    if number % 2 != 0:
        continue
    print(number)


n = int(input('Enter a number: '))

for number in range(1, n + 1):
    if number % 2 == 0:
        continue
    print(number)


# Verificar se o ano é bissexto
year = 2000

if year % 400 == 0:
    result = 'leap year'
elif year % 100 == 0:
    result = 'not a leap year'
elif year % 4 == 0:
    result = 'leap year'
else:
    result = 'not a leap year'
print(result)

# outra maneira de fazer
year = 2000

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    result = 'leap year'
else:
    result = 'not a leap year'
