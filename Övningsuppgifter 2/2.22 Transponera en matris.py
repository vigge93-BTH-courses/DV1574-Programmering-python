def transpose(matrix):
    res = []
    for i, val_i in enumerate(matrix):
        for j, val_j in enumerate(val_i):
            if len(res) <= j:
                res.append([val_j])
            else:
                res[j].append(val_j)
    return res


print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([[1, 2]]))
print(transpose([[3]]))
