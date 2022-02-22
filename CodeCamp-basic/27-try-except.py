
value = 12

try:
    value = 10
    number = int(input("Enter number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")

print()