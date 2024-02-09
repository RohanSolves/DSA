'''Time Complexity	 
    Best	O(nlogn)
    Worst	O(nlogn)
    Average	O(nlogn)
Space Complexity	O(1)'''

def heapify(arr, n, i):
    # Find largest among root and children
    rootNode = i
    leftNode = 2 * i+ 1     #  Find position of leftNode
    rightNode = 2 * i + 2   #  Find position of rigtNode
  
    if leftNode < n and arr[i] < arr[leftNode]:
        rootNode = leftNode
  
    if rightNode < n and arr[rootNode] < arr[rightNode]:
        rootNode = rightNode
  
    # If root is not largest, swap with largest and continue heapifying
    if rootNode != i:
        arr[i], arr[rootNode] = arr[rootNode], arr[i]
        heapify(arr, n, rootNode)
  
  
def heapSort(arr):
    n = len(arr)
  
    # Build max hea
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
  
        # Heapify root element
        heapify(arr, i, 0)
  

# Driver Code
arr = [19, 22, 12, 9, 25, 60, 10]
heapSort(arr)
n = len(arr)

print("Sorted array is: ")
for i in range(n):
    # print("%d " % arr[i], end='')
    print(arr[i], end=' ')