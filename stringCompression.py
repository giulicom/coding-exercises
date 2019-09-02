# TODO: avoid double loop and useless array "switches" and add conditions to compute everything in one loop
def compress(s):
    switches = []
    for i in range(1,len(s)):
         if s[i] != s[i-1]:
             switches.append(i)
    newS = ""
    for i,switch in enumerate(switches):
        newS += s[switch-1]

        if i == 0:
            newS += str(switch)
        else:
            newS += str(switch-switches[i-1])

    newS += s[-1]
    newS += str(len(s)-switches[-1])

    return newS

if __name__ == '__main__':
    """
    E.g.
    Input: "aabccc"
    Output: "a2b1c3"
    """
    s = "aaabcccdrommmmaammooooree"
    print(compress(s))