def addition_subtraction():
  """
  This function takes two numbers as input from the user,
  performs addition and subtraction, and displays the results.
  """
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    addition_result = num1 + num2
    subtraction_result = num1 - num2

    print(f"Addition result: {addition_result}")
    print(f"Subtraction result: {subtraction_result}")

  except ValueError:
    print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
  addition_subtraction()