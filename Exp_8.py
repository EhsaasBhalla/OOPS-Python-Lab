def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of a {rows}x{cols} matrix row by row:")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element for row {i+1}, column {j+1}: "))
            row.append(value)
        matrix.append(row)
    return matrix

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Matrix 1:")
matrix1 = input_matrix(rows, cols)

print("Matrix 2:")
matrix2 = input_matrix(rows, cols)

result = add_matrices(matrix1, matrix2)
for row in result:
    print(row)
