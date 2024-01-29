public class BinarySearch {

    // Array sorting
    public static void sortArray(int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] < arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }

    // Print Array
    public static void printArr(int arr[]) {
        // printArray
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    // Binary Search
    public static int binarySearch(int arr[], int num, int i, int j) {
        while (i <= j) {
            int mid = i + (j - i) / 2;
            if ( arr[mid] == num) {
                return mid;
            }
            else if (arr[mid] < num) {
                // return binarySearch(arr, num, mid + 1, j);
                i = mid + 1;
            } else { 
                // return binarySearch(arr, num, mid - 1, j);
                j = mid - 1;
            }
        }
        return -1;
    }

    public static int binarySum(int arr[], int sum, int i, int j) {
        int lNum = arr[0];
        int rNum = arr.length - 1;

        while (i <= j) {
            if (sum == arr[i] + arr[j]) {
                return i & j;
            }
            else if (sum > arr[i] + arr[j]) {
                rNum = rNum - 1;
            }
            else {
                lNum = lNum + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int arr[] = { 20, 45, 27, 47, 55, 67, 75, 88, 90 };
        // int num = 27;
        sortArray(arr);
        // printArr(arr);
        // System.out.println();

        // int result = binarySearch(arr, num, 0, arr.length - 1);
        // if (result == -1) {
        //     System.out.println("The number not found");
        // } else {
        //     System.out.println("Number found at " + result);
        // }

        int numSum = 118;
        int result = binarySum(arr, numSum, 0, arr.length - 1);
        if (result == -1)  {
            System.out.println("Sum not found...");
        } else {
            System.out.println("Sum is found at position " + result);
        }
    }
}
