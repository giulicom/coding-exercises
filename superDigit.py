#!/bin/python3

def superDigit(n, k):
    if k == 0:
        return n

    newN = sum(n)
    newN = [int(x) for x in list(str(newN))]

    return superDigit(newN, k-1)

if __name__ == '__main__':

    """
    N = 148148148
    super_digit(N) = super_digit(148148148) 
               = super_digit(1+4+8+1+4+8+1+4+8)
               = super_digit(39)
               = super_digit(3+9)
               = super_digit(12)
               = super_digit(1+2)
               = super_digit(3)
               = 3.
    """
    n = 148
    k = 3

    toSum = [int(x) * k for x in list(str(n))]
    result = superDigit(toSum, k)
    print(result[0])

