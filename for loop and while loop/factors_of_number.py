number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Factors of {number}:")
    for factor in range(1, number + 1):
        if number % factor == 0:
            print(factor)
