def fib(n):
    fibArr = [0, 1]
    while len(fibArr) <= n:
        fibArr.append(0)

    if n == 0: return fibArr[0]
    elif n == 1: return fibArr[1]
    else:
        fibArr[n] = fib(n-1) + fib(n-2)
        return fibArr[n]

def optmisedFib(n):
    if n < 0: return -1
    else:
        if n == 0: return 0
        elif n == 1: return 1
        else:
            min2 = 0
            min1 = 1
            for i in range(2,n+1):
                last = min2 + min1
                min2 = min1
                min1 = last
            return last


if __name__ == '__main__':

    n = 9
    print(optmisedFib(n))