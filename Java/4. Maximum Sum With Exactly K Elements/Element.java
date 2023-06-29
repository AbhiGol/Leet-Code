import java.util.Arrays;

public class Element {
    public static void main(String[] args) {
        int[] nums = { 4, 2, 9, 7, 6 };
        int k = 3;

        int maxSum = findMaximumSum(nums, k);

        System.out.println("Maximum sum with exactly " + k + " elements: " + maxSum);
    }

    public static int findMaximumSum(int[] nums, int k) {
        if (k > nums.length) {
            System.out.println("Invalid input: K is greater than the array size.");
            return 0;
        }

        Arrays.sort(nums);
        int maxSum = 0;

        for (int i = nums.length - 1; i >= nums.length - k; i--) {
            maxSum += nums[i];
        }

        return maxSum;
    }
}
