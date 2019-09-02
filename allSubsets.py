def allSubsets(s):
    res = [[]]
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            res.append(list(sub))

    return res


if __name__ == '__main__':
    s = "giulia"
    res = allSubsets(s)
    print(res)
    print(len(res))