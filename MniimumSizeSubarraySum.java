public class MniimumSizeSubarraySum {

    public int minSubArrayLen(int s, int[] nums) {
        int minSize = Integer.MAX_VALUE;
        int currSum = 0;
        int start = 0;
        for (int i = 0; i < nums.length; i++) {
            currSum += nums[i];
            while (currSum >= s) {
                minSize = Math.min(minSize, i + 1 - start);
                currSum -= nums[start++];
            }
        }
        return (minSize != Integer.MAX_VALUE) ? minSize : 0;
    }

}
