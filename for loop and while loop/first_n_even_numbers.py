count = int(input("How many even numbers should be printed? "))

if count < 0:
    print("The count cannot be negative.")
else:
    for index in range(1, count + 1):
        print(index * 2)
