number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Negative numbers are not strong numbers.")
else:
    digit_factorial_sum = 0
    for digit_character in str(number):
        digit = int(digit_character)
        factorial = 1
        for factor in range(1, digit + 1):
            factorial *= factor
        digit_factorial_sum += factorial

    if digit_factorial_sum == number:
        print(f"{number} is a strong number.")
    else:
        print(f"{number} is not a strong number.")
