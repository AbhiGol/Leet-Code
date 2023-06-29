public class Digit {
    public static void separateDigits(int[] arr) {
        for (int num : arr) {
            String numStr = String.valueOf(num);

            for (int i = 0; i < numStr.length(); i++) {
                int digit = Character.getNumericValue(numStr.charAt(i));
                System.out.print(digit + " ");
            }

            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[] numbers = { 123, 456, 789 };
        separateDigits(numbers);
    }
}