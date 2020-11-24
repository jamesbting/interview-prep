public class SortColors {
    public void sortColors(int[] nums) {
        if (nums.length == 1)
            return;
        int[] colors = new int[3];
        for (int n : nums)
            colors[n]++;

        int i = 0;
        for (int j = 0; j < 3; j++) {
            while (i < nums.length && colors[j] > 0) {
                nums[i++] = j;
                colors[j]--;
            }
        }
    }
}
