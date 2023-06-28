public class insert {
    public static void main(String[] args) {
        int[] nums = { 1, 3, 5, 6 };
        int target = 4;

        int insertPosition = searchInsert(nums, target);

        System.out.println("Insert position: " + insertPosition);
    }

    public static int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        // If the target is not found, left will be the correct insert position
        return left;
    }
}
