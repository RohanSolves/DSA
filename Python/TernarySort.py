# Example for the ternary serch
# Time complexity (nlogn)
def TernarySort(arr, i, j, target):
    mid1 = i + (j - i) // 3
    mid2 = j - (j - i) // 3

    while (i <= j):
        if (arr[mid1] == target):
            return mid1
        elif (arr[mid2] == target):
            return mid2
        elif (target > arr[mid2]):
            return TernarySort(arr, mid2 + 1, j, target)
        elif (target < arr[mid1]):
            return TernarySort(arr, i, mid1 - 1, target)
        else:
            return TernarySort(arr, mid1 + 1, mid2 - 1, target)
    return -1

arr = [22, 24, 6, 18, 10, 12, 14, 80, 90, 120, 240]
target = 14
i = 0
j = len(arr) - 1

result = TernarySort(arr, i, j, target)
print(result)
