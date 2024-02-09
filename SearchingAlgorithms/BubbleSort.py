# Method Definition
def BubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr) - 1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

# Driver Code
arr = [20, 3, 55, 45, 47, 55, 67, 75, 88, 90]
result = BubbleSort(arr)
print(result)