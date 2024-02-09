''' To find weather the sum of two numbers equals 
to target value or not using Two Pointer Approach... '''

''' Time Complexity --> O(n)'''

# Method Definition
def BinarySum(arr, target, left, right):
    
    while left <= right:
        targetSum = arr[left] + arr[right]
        if targetSum == target:
            return left, right
        elif targetSum < target:
            left = left + 1
        else:
            right = right - 1
    return -1, -1

# Driver Code
arr = [20, 45, 47, 55, 67, 75, 88, 90]
target = 100
left = 0
right = len(arr) - 1

result = BinarySum(arr, target,left, right)
print(result)