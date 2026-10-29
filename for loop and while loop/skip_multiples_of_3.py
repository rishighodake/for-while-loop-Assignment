limit = int(input("Print numbers from 1 up to: "))

for number in range(1, limit + 1):
    if number % 3 != 0:
        print(number)
