collection= ["Style", "Nishat", "Ocean", "Zulbery"]
for x in collection:
    print(x)

iterator = iter(collection)
while True:
    try:
        x = next(iterator)
        print(x)
    except StopIteration:
        break