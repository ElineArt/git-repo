def multiplication_division():
  
  try:
    num1 = float(input("Please type your first number: "))
    num2 = float(input("Please type your second number: "))

    multiplication_result = num1 * num2

    if num2 != 0:
      division_result = num1 / num2
      print(f"The result of the division is: {division_result}")
    else:
      print("It is not allowed to divide  by zero.")
      division_result = "Undefined"

    print(f"This is the result for the multiplication: {multiplication_result}")

  except ValueError:
    print("This is an invalid input. Try again.")

if __name__ == "__main__":
  multiplication_division()
