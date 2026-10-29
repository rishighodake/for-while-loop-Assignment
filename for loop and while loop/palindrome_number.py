number = int(input("Enter an integer: "))

if number < 0:
    is_palindrome = False
else:
    original = number
    remaining = number
    reversed_number = 0

    while remaining > 0:
        digit = remaining % 10
        reversed_number = reversed_number * 10 + digit
        remaining //= 10

    is_palindrome = original == reversed_number

if is_palindrome:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
