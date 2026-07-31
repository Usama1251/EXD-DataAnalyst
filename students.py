try:
    print("------------ Student Management System ------------\n")

    print("1- Add Student")
    print("2- Display Students")
    print("3- Search Student")
    print("4- Update Student")
    print("5- Exit")

    x = int(input("\nEnter your choice: "))

    if x == 1:
        name = input("Enter student name: ")

        if not name.replace(" ", "").isalpha():
            raise ValueError("Student name should contain only alphabets.")

        try:
            with open("students.txt", "r") as f:
                student_id = sum(1 for line in f) + 1
        except FileNotFoundError:
            student_id = 1

        with open("students.txt", "a") as f:
            f.write(f"{student_id}- {name}\n")

        print("Student added successfully!")

    elif x == 2:
        try:
            with open("students.txt", "r") as f:
                print("\n------ Student List ------")
                data = f.read()

                if data:
                    print(data)
                else:
                    print("No student records found.")

        except FileNotFoundError:
            print("Student file does not exist.")

    elif x == 3:
        search = input("Enter student name to search: ").lower()

        found = False

        try:
            with open("students.txt", "r") as f:
                for line in f:
                    if search == line.split("-")[1].strip().lower():
                        print("Student Found!")
                        print(line.strip())
                        found = True
                        break

            if not found:
                print("No such student found.")

        except FileNotFoundError:
            print("Student file not found.")

    elif x == 4:
        old_name = input("Enter old student name: ").lower()
        new_name = input("Enter new student name: ")

        if not new_name.replace(" ", "").isalpha():
            raise ValueError("Student name should contain only alphabets.")

        found = False

        try:
            with open("students.txt", "r") as f:
                lines = f.readlines()

            with open("students.txt", "w") as f:
                for line in lines:

                    if old_name == line.split("-")[1].strip().lower():
                        student_id = line.split("-")[0]
                        f.write(f"{student_id}- {new_name}\n")
                        found = True
                    else:
                        f.write(line)

            if found:
                print("Student updated successfully!")
            else:
                print("No such student found!")

        except FileNotFoundError:
            print("Student file not found.")

    elif x == 5:
        print("Exiting Program...")

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)

else:
    print("Operation completed successfully!")

finally:
    print("Thank you for using Student Management System.")