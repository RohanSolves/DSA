public class TwoBinarySearch {

    public static void printArray(int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static int[] addNum(int arr[], int target_sum, int i, int j) {
        int left = 0;
        int right = arr.length - 1;

        while (i <= j) {
            if (arr[left] + arr[right] == target_sum) {
                int result[] = {right, left};
                return result;
            } else if (arr[left] + arr[right] > target_sum) {
                right = right - 1;
            } else if (arr[left] + arr[right] < target_sum) {
                left = left + 1;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        int arr[] = { 20, 40, 60, 80, 90, 120, 240};
        printArray(arr);
        System.out.println();
        int target_sum = 240;
        
        int finalResult[] = addNum(arr, target_sum, 0, arr.length - 1);
        if (finalResult == null) {
            System.out.println("Sum is not found"); 
        } else {
            System.out.println("Sum found at positions: " + finalResult);
        }
    }
}
