number = [3,2,4,1,5,9,2,6]
for n in reversed(number):
    print(n)

print("== Sort ==")

for n in sorted(number):
    print(n)
    
print("== Sort in descending ==")

for n in sorted(number, reverse=True):
    print(n)