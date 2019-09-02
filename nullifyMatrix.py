def setZeros(matrix):
    rows = [False for _ in range(len(matrix))]
    cols = [False for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True

    for i,row in enumerate(rows):
        if row == True:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

    for j,col in enumerate(cols):
        if col == True:
            for i in range(len(matrix)):
                matrix[i][j] = 0


if __name__ == '__main__':
    """
    E.g.
    Input: [[1,2,0],[0,4,5],[5,2,1]]
    Output: [[0, 0, 0], [0, 0, 0], [0, 2, 0]]
    """
    matrix = [[1,2,0],[0,4,5],[5,2,1]]

    setZeros(matrix)

    print(matrix)