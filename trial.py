def setZeroes(matrix):
    foundzero = 0
    zi=-1
    zj=-1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == 0):
                foundzero = 1
                zi = i
                zj = j
                break
        if (foundzero):
            break
    if (foundzero == 0):
        return matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == 0):
                matrix[i][zj] = 0
                matrix[zi][j] = 0
    for i in range(len(matrix)):
        if ((matrix[i][zj] == 0) and (i != zi)):
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
    for i in range(len(matrix[0])):
        if ((matrix[zi][i] == 0) and (i != zj)):
            for j in range(len(matrix)):
                matrix[j][i] = 0
    for i in range(len(matrix)):
        matrix[i][zj] = 0
    for i in range(len(matrix[0])):
        matrix[zi][i] = 0
    return matrix

m = int(input("enter m: "))
n = int(input("enter n: "))
matrix = []
for i in range(m):
    t = []
    for j in range(n):
        x = int(input())
        t.append(x)
    matrix.append(t)

matrixnew = setZeroes(matrix)

for i in range(m):
    s = ""
    for j in range(n):
        s = s + str(matrix[i][j]) + " "
    print(s)