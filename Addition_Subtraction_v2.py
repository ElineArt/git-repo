def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("This is not a number, try again.")

def main():
    print("Welcome to the Addition and Subtraction Program!")

    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        addition = num1 + num2
        subtraction = num1 - num2

        print("\nResults:")
        print(f"The addition result is: {num1} + {num2} = {addition}")
        print(f"The subtraction result is: {num1} - {num2} = {subtraction}")

        choice = input("\nWould you like to continue with another operation? (Y/N): ").strip().upper()
        if choice != "Y":
            break

    print("Until next time!")

if __name__ == "__main__":
    main()