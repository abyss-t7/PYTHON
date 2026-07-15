dic = [
    {"name": "Asim", "Score": 97},
    {"name": "Ali", "Score": 95},
    {"name": "Kali", "Score":59}]

for v in sorted(dic, key=lambda x:x["Score"]):
    if v["Score"] > 80:
        print(v["name"], v["Score"])
    