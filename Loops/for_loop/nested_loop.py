# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i*j}")
        
tables = [(i, j, i*j) for i in range(1,4) for j in range(1, 4)]

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

flat = [num for row in matrix for num in row]
print(flat)