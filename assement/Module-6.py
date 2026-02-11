def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    grade = calculate_grade(marks)
    print(f"{name}'s grade is {grade}")

while True:
    print("\n--- Grade Management System ---")
    print("1. Add Student")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again!")
