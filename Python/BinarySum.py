def binarySum(arr, target):
    left = 0;
    right = len(arr) - 1
    while (left <= right):
        if (arr[left] + arr[right] == target):
            return left, right
        elif (arr[left] + arr[right] > target):
            right = right - 1
        else:
            left = left + 1
    return -1, -1

arr = [22, 24, 6, 18, 10, 12, 14]
target = 32
result = binarySum(arr, target)
print(result)