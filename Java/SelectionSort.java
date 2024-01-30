public class SelectionSort {

    public static void selectionSort(int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            int min_idx = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[min_idx]) {
                    min_idx = j;
                }
            }
            int temp = arr[i];
                arr[i] = arr[min_idx];
                arr[min_idx] = temp;
        }
    }

    public static void printArray(int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int arr[] = { 7, 4, 10, 11, 16, 20, 5, 1 };

        printArray(arr);
        selectionSort(arr);
        printArray(arr);
    }
}
