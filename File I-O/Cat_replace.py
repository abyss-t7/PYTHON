word = "Donkey"

with open("/mnt/8c04d511-6bcd-4d60-8be1-5ea58b6e4015/5 Goal_Dream_Aim/PYTHON/File I-O/Cat.txt", "r") as j: 
    content = j.read()
    content = content.replace("Cat", "Dog")

print(content)