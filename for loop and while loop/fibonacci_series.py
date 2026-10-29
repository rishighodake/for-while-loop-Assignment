terms = int(input("Enter the number of Fibonacci terms: "))

if terms < 0:
    print("The number of terms cannot be negative.")
else:
    first, second = 0, 1
    for _ in range(terms):
        print(first, end=" ")
        first, second = second, first + second
    print()
