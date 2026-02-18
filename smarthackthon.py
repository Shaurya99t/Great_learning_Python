class SpeciallyAbledStudent:
    def __init__(self, student_id, name, disability_type):
        self.student_id = student_id
        self.name = name
        self.disability_type = disability_type
        self.needs = []
        self.progress = 0

    def add_need(self, need):
        self.needs.append(need)

    def update_progress(self, progress):
        self.progress = progress

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def admit_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"Students at {self.name}:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Disability Type: {student.disability_type}")

def main():
    school_name = input("Enter the name of the school: ")
    school = School(school_name)

    while True:
        print("\nOptions:")
        print("1. Admit a specially-abled student")
        print("2. Display students in the school")
        print("3. Exit")
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
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
