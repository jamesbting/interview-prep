public class JumpGame {

    public boolean canJump(int[] nums) {
        int lastPos = nums.length - 1; // last reachable position

        // check each position, and see if it can reach the last reachable position or
        // further
        // if so the current position becomes the last reachable position
        for (int i = nums.length - 1; i >= 0; i--)
            if (i + nums[i] >= lastPos)
                lastPos = i;

        return lastPos == 0; // check if the last reachable position was 0
    }
}
