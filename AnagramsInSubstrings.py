from collections import Counter
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        a = []
        for j in range(len(s)-i+1):
            a.append("".join(sorted(s[j:j+i])))
        b = Counter(a)
        print(b)
        for j in b:
            count+=b[j]*(b[j]-1)/2
    return int(count)


if __name__ == '__main__':
    s = "annamariai"

    res = sherlockAndAnagrams(s)
    print(res)