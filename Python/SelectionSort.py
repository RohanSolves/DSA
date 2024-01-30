# actual funtion
def selectionSort(arr):
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if (arr[j] < arr[min_idx]):
                min_idx = j
        # swap the values
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# funtion calling
arr = [70, 56, 23, 19, 25, 37, 48]
print("Array before sort", arr)
result = selectionSort(arr)
print("Array after selection Sort", result)
