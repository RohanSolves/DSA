public class StockMonitor {

    public static double findMaxProfit(int arr[]) {
        double maxProfit = 0;
        double minPrice = Double.MAX_VALUE;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < minPrice) {
                minPrice = arr[i];
            } else if (arr[i] - minPrice > maxProfit) {
                maxProfit = arr[i] - minPrice;
            }
        }

        return maxProfit;
    }

    public static void main(String[] args) {
        int arr[] = { 7, 4, 5, 1, 6, 16};
        double result = findMaxProfit(arr);
        System.out.println(result);
    }
}
