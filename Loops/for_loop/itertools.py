from itertools import chain, product, combinations, permutations

list1 = [1,2,3]
list2 = [4,5,6]
for i in chain(list1, list2): # no nested loop
    print(i)
    
print("== product ==")

color = ["green", "red", "blue"]
size = ["S", "M", "L"]
for color, size in product(color, size): # cartesian product like nested for loop
    print(color, size)
    
print("== product ==")

players = ["A", "B", "C", "D"]
for pair in combinations(players, 2):# choose r item, order doesn't matter 
    print(pair)
    
print("== permutation ==")

for p in permutations(["X", "Y", "Z"], 2):
    print(p)