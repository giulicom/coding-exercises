def checkParenthesis(s):
    right_left_map = {")":"(", "]":"[", "}":"{"}
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


if __name__=='__main__':
    s = ")))"
    print(checkParenthesis(s))