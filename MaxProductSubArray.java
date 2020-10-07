//https://leetcode.com/problems/maximum-product-subarray/

class MaxProductSubArray {
    public int maxProduct(int[] nums) {
        if (nums.length == 1)
            return nums[0];

        int maxEndingHere = 1;
        int minEndingHere = 1;
        boolean maxGreaterThan0 = true;
        int max = Integer.MIN_VALUE;
        for (int i : nums) {
            int temp = maxEndingHere;
            maxEndingHere = Integer.max(i, Integer.max(maxEndingHere * i, minEndingHere * i));
            minEndingHere = Integer.min(i, Integer.min(minEndingHere * i, temp * i));
            max = Integer.max(maxEndingHere, max);
        }
        return max;
    }
}