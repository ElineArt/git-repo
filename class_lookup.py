print("Welcome to Eline’s CSU Class Lookup Tool.")

# Define dictionaries
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Loop for course lookup
while True:
    course_num = input("Enter a course number (e.g., CSC101): ").upper()

    if course_num not in course_rooms:
        print("Invalid course number. Please try again.")
    else:
        print(f"Course: {course_num}")
        print(f"Room Number: {course_rooms[course_num]}")
        print(f"Instructor: {course_instructors[course_num]}")
        print(f"Meeting Time: {course_times[course_num]}")

    # Ask if user wants to continue
    again = input("Would you like to look up another class? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break