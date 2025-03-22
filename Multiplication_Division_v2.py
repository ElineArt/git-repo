def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("This is not a number, try again.")

def main():
    print("Welcome to the Multiplication and Division Program!")

    while True:
        num1 = get_number("Enter the first number: ")

        while True:
            num2 = get_number("Enter the second number: ")
            if num2 == 0:
                print("Cannot divide by zero, try again.")
            else:
                break

        multiplication = num1 * num2
        division = num1 / num2

        print("\nResults:")
        print(f"The multiplication result is: {num1} * {num2} = {multiplication}")
        print(f"The division result is: {num1} / {num2} = {division}")

        choice = input("\nWould you like to continue with another operation? (Y/N): ").strip().upper()
        if choice != "Y":
            break

    print("Until next time!")

if __name__ == "__main__":
    main()