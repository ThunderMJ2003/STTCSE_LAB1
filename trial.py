"""module for STTCSE LAB 1"""

def set_zeroes(matrix):
    """funtion to set the rows and columns zero if the matrix has zero there"""
    foundzero = 0
    zi=-1
    zj=-1
    for i, mi in enumerate(matrix):
        for j, mj in enumerate(mi):
            if mj == 0:
                foundzero = 1
                zi = i
                zj = j
                break
        if foundzero:
            break
    if foundzero == 0:
        return matrix
    for i, mi in enumerate(matrix):
        for j, mj in enumerate(mi):
            if mj == 0:
                matrix[i][zj] = 0
                matrix[zi][j] = 0
    for i, mi in enumerate(matrix):
        if ((mi[zj] == 0) and (i != zi)):
            for j, mj in enumerate(mi):
                mj = 0
    for i, mi in enumerate(matrix[0]):
        if ((matrix[zi][i] == 0) and (i != zj)):
            for j, mj in enumerate(matrix):
                matrix[j][i] = 0
    for i, mi in enumerate(matrix):
        mi[zj] = 0
    for i, mi in enumerate(matrix[0]):
        matrix[zi][i] = 0
    return matrix

m = int(input("enter m: "))
n = int(input("enter n: "))
matrixinp = []
for a in range(m):
    t = []
    for b in range(n):
        x = int(input())
        t.append(x)
    matrixinp.append(t)

matrixnew = set_zeroes(matrixinp)

for a in range(m):
    st = ""
    for b in range(n):
        st = st + str(matrixnew[a][b]) + " "
    print(st)
