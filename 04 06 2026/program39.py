A = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for j in range(len(A[0])):
    row = []
    for i in range(len(A)):
        row.append(A[i][j])
    transpose.append(row)

print("Transpose of matrix:")
for row in transpose:
    print(row)
