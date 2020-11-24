public class 3Sum {
   
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for(int i = 0; i < nums.length - 2; i++) {
            if(i > 0 && nums[i] == nums[i-1]) continue;
            int n = nums[i];
            int low = i + 1;
            int high = nums.length - 1;
            while(low < high) {
                if(nums[low] + nums[high] == -1 * n) {
                    res.add(Arrays.asList(nums[low], nums[high], n));
                    while(high > 0 && nums[high] == nums[high-1]) high--;
                    while(low < nums.length -1 && nums[low] == nums[low + 1]) low++;
                    low++;
                    high--;
                } else if(nums[low] + nums[high] > -1 * n) {
                    high--;
                } else if(nums[low] + nums[high] < -1 * n) {
                    low++;
                }
            }
        }
        
        return res;
    }
}
