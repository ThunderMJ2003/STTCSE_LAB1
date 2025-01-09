"""module for STTCSE LAB 1"""

def set_zeroes(matrix):
    """Function to set the rows and columns to zero if the matrix has a zero."""
    m, n = len(matrix), len(matrix[0]) if matrix else 0
    zero_rows, zero_cols = set(), set()

    # Step 1: Identify all rows and columns that need to be set to zero
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Step 2: Set rows to zero
    for row in zero_rows:
        for j in range(n):
            matrix[row][j] = 0

    # Step 3: Set columns to zero
    for col in zero_cols:
        for i in range(m):
            matrix[i][col] = 0

    return matrix

# Input handling
m = int(input("Enter m: "))
n = int(input("Enter n: "))
matrixinp = []

for _ in range(m):
    row = list(map(int, input().split()))
    matrixinp.append(row)

# Process and output result
matrixnew = set_zeroes(matrixinp)

for row in matrixnew:
    print(" ".join(map(str, row)))
