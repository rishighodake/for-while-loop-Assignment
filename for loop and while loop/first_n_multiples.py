number = int(input("Enter the number: "))
count = int(input("How many multiples should be printed? "))

if count < 0:
    print("The count cannot be negative.")
else:
    for multiplier in range(1, count + 1):
        print(f"{number} x {multiplier} = {number * multiplier}")
