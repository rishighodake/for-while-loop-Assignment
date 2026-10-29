number = int(input("Enter an integer: "))
remaining = abs(number)
reversed_number = 0

while remaining > 0:
    digit = remaining % 10
    reversed_number = reversed_number * 10 + digit
    remaining //= 10

if number < 0:
    reversed_number = -reversed_number

print(f"Reversed number: {reversed_number}")
