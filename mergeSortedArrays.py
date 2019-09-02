def mergeSortedArrays(A, B):
    lastEmpty = len(A)-1
    lastA = -1
    for i in range(len(A)-1, -1, -1):
        if A[i] != None:
            lastA = i
            break

    lastB = len(B)-1

    while lastA >= 0 and lastB >= 0:
        if A[lastA] > B[lastB]:
            A[lastEmpty] = A[lastA]
            lastA -= 1
            lastEmpty -=1
        else:
            A[lastEmpty] = B[lastB]
            lastB -= 1
            lastEmpty -= 1

    while lastB >= 0:
        A[lastEmpty] = B[lastB]
        lastB -= 1
        lastEmpty -= 1

    return A


if __name__ == '__main__':
    A = [1,3,6,9,None,None,None]
    B = [0,4,10]

    print(mergeSortedArrays(A,B))