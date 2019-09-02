def palindromePartitioning(s, elements, res):

    if not s:
        return res.append(elements)

    for i in range(1,len(s)+1):
        if isPotentialPalindromel(s[:i]):
            newEl = elements + [s[:i]]
            palindromePartitioning(s[i:], newEl, res)

def isPotentialPalindrome(s):
    counts = {}
    for el in s:
        if el in counts:
            counts[el] += 1
        else:
            counts[el] = 1

    odds = 0
    for k, v in counts.items():
        if v % 2 != 0:
            odds += 1

        if odds > 1:
            return False
    return True

if __name__ == '__main__':
    s = "anna"
    elements = []
    res = []

    palindromePartitioning(str.join("",sorted(s)), elements, res)
    print(res)
