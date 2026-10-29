base = float(input("Enter the base: "))
exponent = int(input("Enter an integer exponent: "))

if base == 0 and exponent < 0:
    print("Zero cannot be raised to a negative power.")
else:
    result = 1
    for _ in range(abs(exponent)):
        result *= base

    if exponent < 0:
        result = 1 / result

    print(f"{base} raised to {exponent} = {result}")
