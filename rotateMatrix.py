# def rotate(matrix):
#
#     l = len(matrix)
#     # flip it
#     for i in range(l // 2):
#         matrix[i], matrix[l - i - 1] = matrix[l - i - 1], matrix[i]
#     # transpose it
#     for j in range(l):
#         for i in range(j, l):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def rotate(matrix):
    N = len(matrix)
    for i in range(N//2):
        for j in range(i, N-1-i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N-1-j][i]
            matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
            matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
            matrix[j][N-1-i] = temp

if __name__ == '__main__':
    """
    Rotate a matrix of 90° (IN PLACE)
    E.g. 
    Input: matrix = [[1,2,3],
                     [4,5,6],
                     [7,8,9]]
                     
    Output: matrix = [[7,4,1],
                      [8,5,2],
                      [9,6,3]]
    """
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    print(matrix)