public class RangeSumOfSortedSubArrays {
    private static int constant = (int) (Math.pow(10, 9) + 7);

    public int rangeSum(int[] nums, int n, int left, int right) {
        int[] sums = new int[n * (n + 1) / 2];
        sums[0] = nums[0];
        int currNum = 1;
        int nextStart = 1;
        for (int i = 1; i < sums.length; i++) {
            if (currNum == nums.length) {
                currNum = nextStart;
                nextStart++;
                sums[i] = nums[currNum];
            } else {
                sums[i] = sums[i - 1] + nums[currNum];
            }
            currNum++;
        }

        int sum = 0;
        Arrays.sort(sums);
        for (int i = left - 1; i <= right - 1; i++) {
            sum = (sum + (sums[i] % constant)) % constant;
        }
        return sum;
    }
}