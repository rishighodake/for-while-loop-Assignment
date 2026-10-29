total = 0

while True:
    number = int(input("Enter a number (0 to finish): "))
    if number == 0:
        break
    total += number

print(f"Sum: {total}")
