# To  find sum of two numbers in array is equal to num or not 
# using binary sort technique...
def two_sum(arr, target_sum):
    left = 0
    right = len(arr) - 1
    while left < right:
        if (arr[left] + arr[right] == target_sum):
            return left, right
        elif (arr[left] + arr[right] > target_sum):
            right = right - 1;
        else:
            left = left + 1
    return -1, -1

arr = [ 20, 40, 60, 80, 90, 120, 240]
target_sum = 210;
result = two_sum(arr, target_sum)
print(result)
