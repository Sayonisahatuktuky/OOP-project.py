class Student:
    def __init__(self, name, roll_number, subjects):
        self.name = name
        self.roll_number = roll_number
        self.subjects = subjects
        self.marks = {subject: None for subject in subjects}

    def input_marks(self):
        for subject in self.subjects:
            while True:
                try:
                    mark = float(input(f"Enter marks for {subject}: "))
                    if 0 <= mark <= 100:
                        self.marks[subject] = mark
                        break
                    else:
                        print("Please enter a mark between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def display_marks(self):
        print("\nMarks:")
        for subject, mark in self.marks.items():
            if mark is not None:
                grade, grade_point, remarks = self.get_grade(mark)
                print(f"{subject}: {mark} - Grade: {grade}, Grade Point: {grade_point}, Remarks: {remarks}")
            else:
                print(f"{subject}: No marks entered")

    def calculate_percentage(self):
        if all(mark is not None for mark in self.marks.values()):
            total_marks = sum(self.marks.values())
            percentage = (total_marks / (len(self.subjects) * 100)) * 100
            return percentage
        else:
            print("Marks for all subjects have not been entered.")
            return None

    def calculate_cgpa(self):
        if all(mark is not None for mark in self.marks.values()):
            total_grade_points = sum(self.get_grade(mark)[1] for mark in self.marks.values())
            cgpa = total_grade_points / len(self.subjects)
            return cgpa
        else:
            print("Marks for all subjects have not been entered.")
            return None

    def get_grade(self, mark):
        if 80 <= mark <= 100:
            return 'A+', 4.00, 'Outstanding'
        elif 75 <= mark < 80:
            return 'A', 3.75, 'Excellent'
        elif 70 <= mark < 75:
            return 'A-', 3.50, 'Very Good'
        elif 65 <= mark < 70:
            return 'B+', 3.25, 'Good'
        elif 60 <= mark < 65:
            return 'B', 3.00, 'Satisfactory'
        elif 55 <= mark < 60:
            return 'B-', 2.75, 'Above Average'
        elif 50 <= mark < 55:
            return 'C+', 2.50, 'Average'
        elif 45 <= mark < 50:
            return 'C', 2.25, 'Below Average'
        elif 40 <= mark < 45:
            return 'D', 2.00, 'Pass'
        else:
            return 'F', 0.00, 'Fail'


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        name = input("Enter student's name: ")
        roll_number = input("Enter student's roll number: ")
        num_subjects = int(input("Enter the number of subjects: "))
        subjects = [input(f"Enter subject {i + 1}: ") for i in range(num_subjects)]
        if roll_number not in self.students:
            student = Student(name, roll_number, subjects)
            self.students[roll_number] = student
            print("Student added successfully.")
        else:
            print("A student with this roll number already exists.")

    def remove_student(self):
        roll_number = input("Enter the roll number of the student to remove: ")
        if roll_number in self.students:
            del self.students[roll_number]
            print("Student removed successfully.")
        else:
            print("No student found with this roll number.")

    def get_student(self):
        roll_number = input("Enter the roll number of the student: ")
        return self.students.get(roll_number)

    def display_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                print(f"\nName: {student.name}, Roll Number: {student.roll_number}")
                student.display_marks()

    def main_menu(self):
        while True:
            print("\n---- Student Management System -----")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Input Marks for a Student")
            print("4. Display Marks for a Student")
            print("5. Calculate Percentage for a Student")
            print("6. Calculate CGPA for a Student")
            print("7. Display All Students")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.remove_student()
            elif choice == '3':
                student = self.get_student()
                if student:
                    student.input_marks()
                else:
                    print("Student not found.")
            elif choice == '4':
                student = self.get_student()
                if student:
                    student.display_marks()
                else:
                    print("Student not found.")
            elif choice == '5':
                student = self.get_student()
                if student:
                    percentage = student.calculate_percentage()
                    if percentage is not None:
                        print(f"Percentage: {percentage:.2f}%")
                else:
                    print("Student not found.")
            elif choice == '6':
                student = self.get_student()
                if student:
                    cgpa = student.calculate_cgpa()
                    if cgpa is not None:
                        print(f"CGPA: {cgpa:.2f}")
                else:
                    print("Student not found.")
            elif choice == '7':
                self.display_all_students()
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.main_menu()
