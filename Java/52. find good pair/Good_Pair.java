public class Good_Pair {
    public static void main(String[] args) {
        int n = 3;
        int k = 3;
        int[] arr = { 1, 4, 3 };
        int sum = 0;
        int count = 0;

        for (int i = 0; i < n; i++) {
            sum = sum + arr[i];
        }

        for (int j = 0; j < n; j++) {
            if (k + arr[j] > sum - arr[j]) {
                count++;
            }
        }
        System.out.println(count);
    }
}
