class Person:
    """Base class representing a person in the university system."""
    def __init__(self, person_id, name, email):
        self._person_id = person_id  # Encapsulated attribute
        self.name = name
        self.email = email

    @property
    def person_id(self):
        return self._person_id

    def get_details(self):
        return f"ID: {self._person_id} | Name: {self.name} | Email: {self.email}"

    def __str__(self):
        return self.name
