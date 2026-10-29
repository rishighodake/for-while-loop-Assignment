count = int(input("How many natural numbers should be printed? "))

if count < 0:
    print("The count cannot be negative.")
else:
    number = 1
    while number <= count:
        print(number)
        number += 1
