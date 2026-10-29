number = abs(int(input("Enter an integer: ")))
digit_product = 1

if number == 0:
    digit_product = 0
else:
    while number > 0:
        digit_product *= number % 10
        number //= 10

print(f"Product of digits: {digit_product}")
