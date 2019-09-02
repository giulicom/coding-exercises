def binarySearhInRotatedArrayRecursive(arr, k, left, right):
    if left <= right:
        mid = (left + right) // 2

        if arr[mid] == k:
            return mid

        if arr[mid] < arr[left] and (k < arr[mid] or k >= arr[left]):
            return binarySearhInRotatedArrayRecursive(arr, k, left, mid - 1)
        elif arr[mid] > arr[right] and (k > arr[mid] or k <= arr[right]):
            return binarySearhInRotatedArrayRecursive(arr, k, mid + 1, right)
        elif k > arr[mid]:
            return binarySearhInRotatedArrayRecursive(arr, k, mid + 1, right)
        else:
            return binarySearhInRotatedArrayRecursive(arr, k, left, mid - 1)

    return -1

def binarySearhInRotatedArray(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == k:
            return mid

        if arr[mid] < arr[left] and (k <= arr[mid] or k >= arr[left]):
            right = mid - 1
        elif arr[mid] > arr[right] and (k > arr[mid] or k <= arr[right]):
            left = mid + 1
        elif k > arr[mid]:
            left = mid +1
        else:
            right = mid -1

    return -1

def binarySearhInRotatedArrayNotDistinct(nums, target):
    # Initilize two pointers
    begin = 0
    end = len(nums) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if nums[mid] == target:
            return True
        if nums[mid] == nums[end]:  # Fail to estimate which side is sorted
            end -= 1  # In worst case: O(n)
        elif nums[mid] > nums[end]:  # Left side of mid is sorted
            if nums[begin] <= target and target < nums[mid]:  # Target in the left side
                end = mid - 1
            else:  # in right side
                begin = mid + 1
        else:  # Right side is sorted
            if nums[mid] < target and target <= nums[end]:  # Target in the right side
                begin = mid + 1
            else:  # in left side
                end = mid - 1
    return False

if __name__ == '__main__':

    arr = [4,5,6,7,0,1,2]
    k = 0

    print(binarySearhInRotatedArrayRecursive(arr,k,0, len(arr)-1))
    print(binarySearhInRotatedArray(arr, k))

    arrNotDistinct = [2,0,1,1,1,2]
    print(binarySearhInRotatedArrayNotDistinct(arrNotDistinct,k))