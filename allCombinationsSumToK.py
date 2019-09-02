def combine(N, R, V, res):

    if R == 0:
        return res.append(V)
    elif R < 0:
        return

    for i in range(1, N):
        newV = V + [i]
        newR = N - sum(newV)
        combine(N, newR, newV, res)

if __name__ == '__main__':
    N = 3
    R = N
    V = []
    res = []

    combine(N, R, V, res)
    print(res)
