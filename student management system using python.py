students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")

        student = {
            "roll": roll,
            "name": name,
            "age": age,
            "course": course,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n--- Student List ---")
            for student in students:
                print("Roll:", student["roll"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])
                print("-------------------")

    # Search Student
    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])
                found = True
                break

        if not found:
            print("Student not found.")

    # Update Student
    elif choice == "4":
        roll = input("Enter Roll Number to update: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                student["name"] = input("Enter new name: ")
                student["age"] = input("Enter new age: ")
                student["course"] = input("Enter new course: ")
                student["marks"] = input("Enter new marks:")

                print("Student updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "5":
        roll = input("Enter Roll Number to delete: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
