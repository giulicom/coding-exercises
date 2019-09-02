def perm(K, seq, prefix, res):
    if K == 0:
        if isBalanced(prefix):
            return res.append(prefix)
        else:
            return res
    for p in seq:
        newP = prefix + p
        perm(K-1, seq, newP, res)

def isBalanced(s):
    right_left_map = {")": "("}
    stack = []
    for p in s:
        if p not in right_left_map.keys():
            stack.append(p)
        else:
            if len(stack) > 0:
                if stack.pop() != right_left_map[p]:
                    return False
            else:
                return False

    if len(stack) > 0:
        return False
    return True

def generateParenthesis(curr, res, n, left, right):
    if right == n:
        return res.append(curr)

    if left < n:
        generateParenthesis(curr+"(", res, n, left+1, right)
    if right < left:
        generateParenthesis(curr+")", res, n, left, right+1)

if __name__ == '__main__':
    n = 3
    seq = "()"
    K = n*2
    prefix = ""
    res = []
    print("Slow method:")
    perm(K, seq, prefix, res)

    print(res)

    print("Fast method:")
    res = []
    generateParenthesis("",res,n,0,0)
    print(res)