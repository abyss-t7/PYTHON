from models.student import Student
from models.instructor import Instructor
from utils.grade_calculator import calculate_gpa, get_letter_grade

def main():
    print("--- University Grade Management System ---")

    # 1. Create Instances (OOP)
    prof = Instructor("INS-001", "Dr. Smith", "smith@uni.edu", "Computer Science")
    prof.assign_course("CS101")
    prof.assign_course("CS102")

    student1 = Student("STU-101", "Asim Ayaz", "asim@uni.edu", "DevOps Engineering")
    student2 = Student("STU-102", "Bruce Wayne", "bruce@uni.edu", "Cybersecurity")

    # 2. Add Grades
    student1.add_grade("CS101", "A")
    student1.add_grade("CS102", "B")
    
    student2.add_grade("CS101", "A")
    student2.add_grade("CS102", "A")

    # 3. Calculate and Display (Using Custom Module)
    for s in [student1, student2]:
        print(f"\nStudent: {s.get_details()}")
        print("Grades:")
        for course, grade in s.grades.items():
            print(f"  - {course}: {grade}")
        
        gpa = calculate_gpa(s.grades)
        print(f"Current GPA: {gpa}")

if __name__ == "__main__":
    main()
