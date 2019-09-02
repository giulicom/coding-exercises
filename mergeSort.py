def merge_sort(arr):

    if len(arr) > 1:
        m = len(arr)//2
        L = arr[:m]
        R = arr[m:]

        merge_sort(L)
        merge_sort(R)

        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [4, 6, 3, 5, 10, 2, 14]
    merge_sort(arr)
