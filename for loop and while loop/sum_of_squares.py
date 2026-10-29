count = int(input("Enter a non-negative integer: "))

if count < 0:
    print("The count cannot be negative.")
else:
    total = 0
    for number in range(1, count + 1):
        total += number * number
    print(f"Sum of squares: {total}")
