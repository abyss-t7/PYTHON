f = open("/mnt/sda4/5 Goal_Dream_Aim/PYTHON/File I-O/poem.txt")
content = f.read()

if("die" in content):
    print("The word die is present")
else:
    print("The word die is not present !")

f.close()