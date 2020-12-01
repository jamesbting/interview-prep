public class PathSum2 {
   /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
    List<List<Integer>> result = new ArrayList<>();
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        dfs(root, 0, sum, new ArrayList<>());
        return result;
    }
    
    private void dfs(TreeNode root, int currSum, int sum, List<Integer> list) {
        
        if(root == null) return;
        
        if(root.left == null && root.right == null && currSum + root.val == sum) {
            list.add(root.val);
            result.add(new ArrayList<>(list));
            list.remove(list.size() -1);
            return;
        }
        
        list.add(root.val);
        dfs(root.left, currSum + root.val, sum, list);
        dfs(root.right, currSum + root.val, sum, list);
        list.remove(list.size() - 1);
    }
}
