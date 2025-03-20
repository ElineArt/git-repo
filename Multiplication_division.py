def multiplication_division():
  """
  This function takes two numbers as input, performs multiplication and division,
  and displays the results. It handles division by zero.
  """
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    multiplication_result = num1 * num2

    if num2 != 0:
      division_result = num1 / num2
      print(f"Division result: {division_result}")
    else:
      print("Division by zero is not allowed.")
      division_result = "Undefined"

    print(f"Multiplication result: {multiplication_result}")

  except ValueError:
    print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
  multiplication_division()