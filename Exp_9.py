def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            product_sum = 0
            for k in range(len(matrix1[0])):
                product_sum += matrix1[i][k] * matrix2[k][j]
            row.append(product_sum)
        result.append(row)
    return result

rows1, cols1 = (int(x) for x in input("Enter dimensions of matrix1 (rows cols): ").split())
print("Enter elements of matrix1:")
matrix1 = [list(int(x) for x in input().split()) for _ in range(rows1)]

rows2, cols2 = (int(x) for x in input("Enter dimensions of matrix2 (rows cols): ").split())
print("Enter elements of matrix2:")
matrix2 = [list(int(x) for x in input().split()) for _ in range(rows2)]


result = multiply_matrices(matrix1, matrix2)
for row in result:
    print(row)
