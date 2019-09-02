def find_common_elements(A, B):

    i = j = 0
    common_els = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            common_els.append(A[i])
            i += 1
            j += 1
        elif A[i] > B[j]:
            j += 1
        else:
            i += 1

    return common_els

if __name__ == '__main__':
    A = [1,12,15,19,21]
    B = [2,15,17,19,21,25,27]

    print(find_common_elements(A,B))

    # time complexity O(B) (longest between the two)
    # space O(1)