# Time Complexity --> O(n)

# Method Definition
def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Driver Code
arr = [20, 45, 27, 47, 55, 67, 75, 88, 90]
target = 55
result = LinearSearch(arr, target)
print(result)