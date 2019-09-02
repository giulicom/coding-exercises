def findKSmallest(arr,k):

    smallest = arr[:k]
    highestSmallest = max(smallest)
    i = k
    while i < len(arr):
        if arr[i] < highestSmallest:
            smallest.remove(highestSmallest)
            smallest.append(arr[i])
            highestSmallest = max(smallest)
        i+=1
    return smallest


if __name__ == '__main__':
    arr = [4,3,5,1,6]
    k = 3
    print(findKSmallest(arr,k))
