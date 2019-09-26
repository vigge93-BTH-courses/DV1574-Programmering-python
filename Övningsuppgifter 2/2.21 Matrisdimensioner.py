def matrix_dimensions(matrix):
    rows = len(matrix)
    if rows == 0:
        return 'This is not a valid matrix'
    cols = len(matrix[0])
    for col in matrix:
        if len(col) != cols or len(col) == 0:
            return 'This is not a valid matrix'

    return 'This is a {}x{} matrix.'.format(rows, cols)


print(matrix_dimensions([[1, 3], [-5, 6], [2, 4]]))
print(matrix_dimensions([[1, 3, 2], [-5, 6, 0]]))
print(matrix_dimensions([[1, 3], [-5, 6, 0]]))
