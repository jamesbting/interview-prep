// https://leetcode.com/problems/set-mismatch/
public class SetMistmatch {
    public int[] findErrorNums(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int[] res = new int[2];
        int sum = 0;
        for(int n : nums) {
            
            if(set.contains(n)) {
                res[0] = n;
            } else {
                set.add(n);
                sum += n;
            }
        }
        res[1] = (nums.length * (nums.length + 1)) / 2;
        res[1] -= sum; 
        return res;
    }
}