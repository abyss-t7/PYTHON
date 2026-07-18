people = [
    {"name": "Asim", "age": 20, "gpa": 3.72},
    {"name": "Ali",  "age": 19, "gpa": 3.50},
    {"name": "Sara", "age": 22, "gpa": 3.90},
]

by_gpa = sorted(people, key=lambda p:p["gpa"])
# print(by_gpa)

by_name = sorted(people, key=lambda p:len(p["name"]))# Sort by name length
# print(by_name)

# by_age= sorted(people, key=lambda p:p["age"])
# print(by_age)

high = list(filter(lambda p:p["gpa"]>3.6, people)) # # Filter GPA above 3.6
print(high)
