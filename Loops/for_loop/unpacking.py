points = [(1, 2), (3, 4), (5, 6)]

for point in points: # without packing
    print(point[0],point[1])
    
for x, y in points: # with packing and is clean
    print(x, y)
    
data = [("Asim", 95, "UET"), ("Ali", 89,"FAST")] # nested tuples
for name, score, uni  in data:
    print(f"{name} from {uni} scored {score} congratulations!")