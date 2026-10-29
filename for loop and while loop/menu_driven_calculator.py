while True:
    print("\nMenu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "5":
        print("Goodbye!")
        break
    elif choice in ("1", "2", "3", "4"):
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))

        if choice == "1":
            print(f"Result: {first + second}")
        elif choice == "2":
            print(f"Result: {first - second}")
        elif choice == "3":
            print(f"Result: {first * second}")
        elif second == 0:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {first / second}")
    else:
        print("Invalid option. Please choose 1 to 5.")
