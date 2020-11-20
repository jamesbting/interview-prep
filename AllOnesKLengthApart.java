public class AllOnesKLengthApart {
    public boolean kLengthApart(int[] nums, int k) {
        if (k == 0)
            return true;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                int j = i + 1;
                while (j < nums.length && nums[j] == 0)
                    j++;
                if (j < nums.length && (j - i - 1) < k)
                    return false;
            }
        }
        return true;
    }
}
