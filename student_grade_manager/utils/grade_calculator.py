"""Custom module for grade calculations."""

def calculate_gpa(grades_dict):
    """Calculates GPA based on a standard 4.0 scale."""
    if not grades_dict:
        return 0.0

    grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    total_points = 0
    valid_courses = 0

    for course, grade in grades_dict.items():
        if grade in grade_points:
            total_points += grade_points[grade]
            valid_courses += 1

    return round(total_points / valid_courses, 2) if valid_courses > 0 else 0.0

def get_letter_grade(score):
    """Converts a numeric score to a letter grade."""
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'
