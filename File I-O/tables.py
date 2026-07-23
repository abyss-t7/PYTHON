def createtables(n):
    table = ""
    for i in range(2, 11):
        table += f"{n} x {i} = {n*i}\n"


    with open(f"/mnt/8c04d511-6bcd-4d60-8be1-5ea58b6e4015/5 Goal_Dream_Aim/PYTHON/File I-O/tables/table_n{n}.txt", "w") as f:
            f.write(table)


for i in range(2, 21):
    createtables(i)