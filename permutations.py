def permutations(nums, K, prefix, res):

    if K == 0:
        #if sum(prefix) == 0: # if we have a certain condition
        return res.append(prefix)
        #else:
        #    return res

    for el in nums:
        #if el not in prefix:
        newPrefix = prefix + [el]
        permutations(nums, K-1, newPrefix, res)

if __name__ == '__main__':
    nums = [0,1,2]
    K = len(nums)
    prefix = []
    res = []

    permutations(nums, K, prefix, res)
    print(res)
