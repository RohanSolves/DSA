# Method Definition
def BinarySearch(arr, i, j, target):
    arr.sort()
    left = i
    right = j
    while i <= j:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Driver Code
arr = [20, 45, 27, 47, 55, 67, 75, 88, 90]
target = 45
i = 0
j = len(arr) - 1
print(arr)

result = BinarySearch(arr, i, j, target)
print(arr)
print(result)

