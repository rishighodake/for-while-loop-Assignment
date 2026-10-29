number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Negative numbers are not Armstrong numbers.")
else:
    digits = str(number)
    power = len(digits)
    digit_sum = 0

    for digit in digits:
        digit_sum += int(digit) ** power

    if digit_sum == number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
