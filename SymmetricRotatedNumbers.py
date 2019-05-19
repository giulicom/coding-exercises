def symmRotationGenerator(arr, K, res):
    if K == 1:
        return res.extend(arr)
    else:
        leftSides = []
        if K % 2 == 0:
            BuildLefts(arr, K//2, "", len(arr), leftSides)
        else:
            BuildLefts(arr, K // 2 + 1, "", len(arr), leftSides)

        BuildRights(K, leftSides, res)
        return res


def BuildLefts(arr, K, prefix, n, leftSides):
    if K == 0:
        leftSides.append(prefix)
        return

    for i in range(n):
        newPrefix = str(prefix) + str(arr[i])
        BuildLefts(arr, K-1, newPrefix, n, leftSides)

def BuildRights(K, leftSides, res):
    for left in leftSides:
        newLeft = left
        if K % 2 != 0 and K > 1 and newLeft[-1] != "6" and newLeft[-1] != "9":
            newLeft = left[:-1]
        if newLeft is not None and newLeft[0] != "0":
            reversedLeft = "".join(list(newLeft)[::-1])
            #if len(reversedLeft) > 0:
            if "6" in newLeft:
                reversedLeft = reversedLeft.replace("6", "9")
            elif "9" in newLeft:
                reversedLeft = reversedLeft.replace("9", "6")

            res.append(left + reversedLeft)

    return res

if __name__ == '__main__':
    arr = ["0", "1", "6", "8", "9"]
    K = 5

    res = []
    for k in range(1, K+1):
        symmRotationGenerator(arr, k, res) # not perfect, there are a few duplicates and problems with numbers with 69/96

    print(sorted([int(el) for el in res]))
    print("Lenght of res: {}".format(len(res)))
