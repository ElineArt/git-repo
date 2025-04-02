# Restaurant Charges Calculator
print("Welcome to the Restaurant Charges Calculator!")
# Step 1 & 2: Get and validate user input
while True:
    try:
        food_charge = float(input("Please enter the charge for the food: $"))
        if food_charge < 0:
            print("Invalid input. Please enter a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
# Step 3: Perform calculations
tip = food_charge * 0.18
tax = food_charge * 0.07
total_price = food_charge + tip + tax
# Step 4: Display results
print(f"\nThe 18% tip is: ${tip:.2f}")
print(f"The 7% sales tax is: ${tax:.2f}")
print(f"The total price is: ${total_price:.2f}")