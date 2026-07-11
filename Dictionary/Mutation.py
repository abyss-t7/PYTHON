data = {
    "Name":"Asim Ayaz",
    "Semester":2,
    "Majors" :"Computer Science",
    "2nd Semester GPA": 3.72,
    "Hobbies":['Solving problems','Swimming','Reading Psychology books','helping others']
}

print(data["Name"])
print(data["Semester"])
print(data["Majors"])
print(data["Hobbies"])

print("== After Mutation ==")

data["Name"] = "Sisyphus"
data["2nd Semester GPA"] = 3.99

print(data["Name"])
print(data["2nd Semester GPA"])


data["Advice"]= "Never Quit hardworking for your goal"

print("==== Printing all data ====",data)# by printing all the new key(advice) will be added in it, called mutation