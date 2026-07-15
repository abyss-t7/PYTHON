names = ["Camus", "Ali", "Ninja"]
score = [95, 88, 91]
grade = ["A", "B+", "A-"]

for name, score, grade in zip(names, score, grade):
    print(f"{name}: {score} ({grade})")

# zip stop at shortest list  
a = [1,2,3,4,5]
b = ["a", "b", "c"]
for x,y in zip(a,b):
    print(x,y) # 4 and 5 are ignored
    