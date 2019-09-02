def antiDiagonalTravers(matrix):
    colStart = rowStart = 0
    M = len(matrix)
    N = len(matrix[0])
    i = j = 0

    res = []

    while colStart < N and rowStart < M:
        j = colStart
        i = rowStart
        path = []
        while i < M and i >= 0 and j < N and j >= 0:
            path.append(matrix[i][j])
            i += 1
            j -= 1

        res.append(path)

        if colStart == N-1:
            rowStart += 1
        else:
            colStart += 1

    return res

if __name__== '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(antiDiagonalTravers(matrix))