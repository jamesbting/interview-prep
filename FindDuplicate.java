//tortose and hare algorithm

public class FindDuplicate {
    public int findDuplicate(int[] nums) {
        int tortoise = nums[0];
        int hare = nums[0];

        // phase 1, find first intersection
        boolean firstLoop = true; // we must ensure that the loop fires at least once, even if tortoise = hare
        while (firstLoop || tortoise != hare) {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
            firstLoop = false;
        }

        // phase 2, find entrance
        tortoise = nums[0];
        while (tortoise != hare) {
            tortoise = nums[tortoise];
            hare = nums[hare];
        }

        return hare;
    }
}
