# 24-Hour Alarm Calculator
print("Welcome to the 24-Hour Alarm Calculator!")
# Step 1: Ask for current time and validate
while True:
    try:
        current_time = int(input("Enter the current time in hours (0 to 23): "))
        if 0 <= current_time <= 23:
            break
        else:
            print("Error: Please enter a valid time between 0 and 23.")
    except ValueError:
        print("Error: Please enter a number.")
# Step 2: Ask for hours to wait and validate
while True:
    try:
        hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
        if hours_to_wait >= 0:
            break
        else:
            print("Error: Please enter a valid positive number of hours.")
    except ValueError:
        print("Error: Please enter a number.")

# Step 3: Add current time and hours to wait
total_hours = current_time + hours_to_wait
# Step 4: Use modulo to stay in 24-hour format
alarm_time = total_hours % 24
# Step 5: Display result
print(f"\nThe alarm will go off at: {alarm_time:02d}:00 on the 24-hour clock.")