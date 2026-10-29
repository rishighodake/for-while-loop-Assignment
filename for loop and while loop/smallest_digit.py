number = abs(int(input("Enter an integer: ")))
smallest = 9

if number == 0:
    smallest = 0

while number > 0:
    digit = number % 10
    if digit < smallest:
        smallest = digit
    number //= 10

print(f"Smallest digit: {smallest}")
