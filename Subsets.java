public class Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> powerSet = new ArrayList<>();
        dfs(nums, powerSet, 0, new ArrayList<Integer>());
        return powerSet;
    }
    
    private void dfs(int[] nums, List<List<Integer>> powerSet, int i, List<Integer> set) {
        powerSet.add(new ArrayList<Integer>(set));
        for(int j = i; j < nums.length; j++) {
            set.add(nums[j]);
            dfs(nums, powerSet, j + 1, set);
            set.remove(set.size() - 1);
        }
    }
}
