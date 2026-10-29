count = int(input("How many odd numbers should be printed? "))

if count < 0:
    print("The count cannot be negative.")
else:
    for index in range(count):
        print(index * 2 + 1)
