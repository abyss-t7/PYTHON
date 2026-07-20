from models.person import Person

class Instructor(Person):
    """Instructor class inheriting from Person."""
    def __init__(self, person_id, name, email, department):
        super().__init__(person_id, name, email)
        self.department = department
        self.courses_taught = []

    def assign_course(self, course_name):
        if course_name not in self.courses_taught:
            self.courses_taught.append(course_name)

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} | Dept: {self.department}"
