f = open("/mnt/8c04d511-6bcd-4d60-8be1-5ea58b6e4015/5 Goal_Dream_Aim/PYTHON/File I-O/poem.txt")
content = f.read()

if("die" in content):
    print("The word die is present")
else:
    print("The word die is not present !")

f.close()