public class First_Missing {
    public static void main(String[] args) {
        int[] nums = { 0, 1, 2, 4 };

        int sum = 0;
        int n = nums.length;
        for (int num : nums) {
            sum += num;
        }
        int arrSum = (((n + 1)) * n) / 2;
        if (arrSum == sum)
            System.out.println("0");
        else
            System.out.println(arrSum - sum);
    }
}
