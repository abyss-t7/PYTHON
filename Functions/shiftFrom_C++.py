def square(x):
    return x * x

def cube(x):
    return x * x * x

transform = square
print(transform(5))   

def apply(func, value):
    return func(value)

print(apply(square, 4))   
print(apply(cube, 3))     

operations = [square, cube, abs]
for op in operations:
    print(op(-3))