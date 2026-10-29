number = int(input("Enter an integer: "))
remaining = abs(number)
largest = 0

while remaining > 0:
    digit = remaining % 10
    if digit > largest:
        largest = digit
    remaining //= 10

print(f"Largest digit: {largest}")
