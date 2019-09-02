def lengthOfLIS(nums):
    ln = len(nums)
    if ln <= 1:
        return ln
    res = 1
    ls = [1] * ln
    for i in range(1, ln):
        j = 0
        while j < i:
            if nums[j] < nums[i]:
                ls[i] = max(ls[i], 1 + ls[j])
            j += 1
        res = max(res, ls[i])

    return res  # or max(ls)

if __name__ == '__main__':
    nums = [10, 9, 2, 150, 3, 7, 191, 18]
    print(lengthOfLIS(nums))