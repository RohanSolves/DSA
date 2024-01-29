import java.util.Scanner;

public class Array {
    public static void main(String[] args) {
        int arr[] = { 20, 45, 27, 47, 55, 67, 75, 88, 90};
        try (Scanner sc = new Scanner(System.in)) {
            int num = sc.nextInt();
            for (int i = 0; i < arr.length; i++){
                if (arr[i] == num) {
                    System.out.println(i);
                }
                // else {
                //     System.out.println("Number not found");
                // }
            }
        }
    }
}