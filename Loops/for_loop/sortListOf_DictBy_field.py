people = [
    {"name": "Asim", "age": 18},
    {"name": "Walter", "age": 42},
    {"name": "CorpL", "age": 24}]
for p in sorted(people, key=lambda x : x["age"]):
    print(p["name"], p["age"])
