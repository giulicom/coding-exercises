def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i = 0
    j = len(height)-1
    area = 0
    while i < j:
        h = min(height[i], height[j])
        currArea = h*(j-i)
        area = max(currArea, area)

        if height[i] > height[j]:
            j -= 1
        else:
            i += 1

    return area

if __name__ == '__main__':
    hist = [1,8,6,2,5,4,8,3,7]

    print(maxArea(hist))