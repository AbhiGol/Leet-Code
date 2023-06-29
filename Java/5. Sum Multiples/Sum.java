public class Sum {
    public static void main(String[] args) {
        int n = 9;
        int sum = 0;

        for (int i = 0; i < n + 1; i++) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                sum = sum + i;
            }
        }
        System.out.println(sum);
    }
}