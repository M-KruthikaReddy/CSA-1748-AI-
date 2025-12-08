matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

transpose_matrix = [[0 for x in range(rows)] for y in range(cols)]

for i in range(rows):
    for j in range(cols):
        transpose_matrix[j][i] = matrix[i][j]

print("Original Matrix:")
for row in matrix:
    print(row)
print("Transposed Matrix:")
for row in transpose_matrix:
    print(row)
