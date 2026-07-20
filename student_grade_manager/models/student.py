from models.person import Person

class Student(Person):
    """Student class inheriting from Person."""
    def __init__(self, person_id, name, email, major):
        super().__init__(person_id, name, email)
        self.major = major
        self.grades = {}  # Dictionary to store course: grade

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} | Major: {self.major}"
