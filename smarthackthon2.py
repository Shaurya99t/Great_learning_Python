# ... (previous code) ...

def main():
    school_name = input("Enter the name of the school: ")
    school = School(school_name)

    while True:
        print("\nOptions:")
        print("1. Admit a specially-abled student")
        print("2. Display students in the school")
        print("3. Update student progress")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            disability_type = input("Enter disability type: ")
            student = SpeciallyAbledStudent(student_id, name, disability_type)
            school.admit_student(student)
            print("Student admitted successfully!")

        elif choice == "2":
            school.display_students()

        elif choice == "3":
            student_id = input("Enter student ID to update progress: ")
            progress = int(input("Enter student's progress: "))
            student = find_student_by_id(student_id)
            if student:
                student.update_progress(progress)
                print("Progress updated successfully!")
            else:
                print("Student not found.")

        elif choice == "4":
            print("Exiting the program.")
            conn.close()
            break

        else:
            print("Invalid choice. Please try again.")

def find_student_by_id(student_id):
    cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    student_data = cursor.fetchone()
    if student_data:
        student = SpeciallyAbledStudent(student_data[1], student_data[2], student_data[3])
        student.update_progress(student_data[4])
        return student
    else:
        return None

if __name__ == "__main__":
    main()
