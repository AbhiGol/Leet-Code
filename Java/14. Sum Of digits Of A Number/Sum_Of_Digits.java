public class Sum_Of_Digits {
    public static void main(String[] args) {
        long sum;
        int n = 123;
        for (sum = 0; n != 0; n /= 10) {
            sum += n % 10;
        }
        System.out.println("Sum of digits of a number is " + sum);
    }
}
