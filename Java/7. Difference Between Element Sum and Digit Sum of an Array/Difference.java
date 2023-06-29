public class Difference {
    public static int getElementSum(int[] arr) {
        int sum = 0;

        for (int num : arr) {
            sum += num;
        }

        return sum;
    }

    public static int getDigitSum(int[] arr) {
        int sum = 0;

        for (int num : arr) {
            String numStr = String.valueOf(num);

            for (char digitChar : numStr.toCharArray()) {
                int digit = Character.getNumericValue(digitChar);
                sum += digit;
            }
        }

        return sum;
    }

    public static void main(String[] args) {
        int[] array = { 23, 456, 71 };
        int elementSum = getElementSum(array);
        int digitSum = getDigitSum(array);
        int difference = elementSum - digitSum;

        System.out.println("Difference: " + difference);
    }
}
