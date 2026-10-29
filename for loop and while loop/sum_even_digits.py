number = int(input("Enter an integer: "))
remaining = abs(number)
digit_sum = 0

while remaining > 0:
    digit = remaining % 10
    if digit % 2 == 0:
        digit_sum += digit
    remaining //= 10

print(f"Sum of even digits: {digit_sum}")
