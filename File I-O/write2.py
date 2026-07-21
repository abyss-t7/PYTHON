with open("/mnt/sda4/5 Goal_Dream_Aim/PYTHON/File I-O/data.txt", "w") as f:
    f.write("Code \n")
    f.write("Deploy \n")
    f.write("Test\n")

lines = ["line1\n", "line2\n", "line3\n"]
with open("/mnt/sda4/5 Goal_Dream_Aim/PYTHON/File I-O/data.txt", "a") as f:
    f.writelines(lines)

with open("/mnt/sda4/5 Goal_Dream_Aim/PYTHON/File I-O/deploy.log", "a") as f:
    f.write("Deployed 21-07-2026\n")