''' Here, we used three pointer approach...
Take array, divide into three parts...
First mid will be mid1 = start + (end - start) // 3
Second mid will be mid2 = end - (end - start) // 3 '''


# Method Definition
def TernarySearch(arr, target, start, end):
    while start <= end:
        mid1 = start + (end - start) // 3
        mid2 = end - (end - start) // 3

        if target == arr[mid1]:
            return mid1
        elif target == arr[mid2]:
            return mid2
        else:
            if target < arr[mid1]:
                return TernarySearch(arr, target, start, mid1 - 1)
            elif target > arr[mid2]:
                return TernarySearch(arr, target, mid2 + 1, end)
            else:
                return TernarySearch(arr, target, mid1 + 1, mid2 - 1)
    return -1

# Driver Code
arr = [20, 30, 35, 45, 47, 55, 67, 75, 88, 90]
target = 75
start = 0
end = len(arr) - 1
result = TernarySearch(arr, target, start, end)
print(result)