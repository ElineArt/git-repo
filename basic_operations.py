def addition_subtraction():
  try:
    num1 = float(input("Please type your first number:  "))
    num2 = float(input("Please type your second number:"))

    addition_result = num1 + num2
    subtraction_result = num1 - num2

    print(f"This is the result for the Addition: {addition_result}")
    print(f"This is the result for the Subtraction: {subtraction_result}")

  except ValueError:
    print("This input is not allowed. Try again.")

if __name__ == "__main__":
  addition_subtraction()