# Row_Number = mid // total columns(n)
# Column_Number = mid % n

def findIn2D(arr, target):
    m = len(arr)     # total number of rows in 2D-array
    if m == 0:
        return False
    n = len(arr[0])  # total number of columns in 2D-array

    left = 0            # initial position of array
    right = m*n - 1     # final position of the array

    while (left <= right):
       mid = left + (right - left) // 2
       mid_element = arr[mid//n][mid%n]
       if (target == mid_element):
           return True
       elif (target < mid_element):
           right = mid - 1
       else:
           left = mid + 1
    return False

arr = [[1, 3, 5, 7], 
       [10, 11, 16, 20], 
       [23, 30, 34, 60]]
target = 3
result = findIn2D(arr, target)
print(result)
