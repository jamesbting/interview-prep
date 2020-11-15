/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode() {} TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left
 * = left; this.right = right; } }
 */

public class MaxLevelSumOfBinaryTree {
    public int maxLevelSum(TreeNode root) {
        HashMap<Integer, Integer> sumsOfLevel = new HashMap<>();
        dfs(root, 1, sumsOfLevel);

        int maxSum = Integer.MIN_VALUE;
        int maxLevel = -1;
        for (int level : sumsOfLevel.keySet()) {
            int sum = sumsOfLevel.get(level);
            if (sum > maxSum) {
                maxSum = sum;
                maxLevel = level;
            }
        }
        return maxLevel;
    }

    private void dfs(TreeNode root, int level, HashMap<Integer, Integer> sumsOfLevel) {
        if (root == null)
            return;

        // need to add a level to arraylist
        sumsOfLevel.put(level, sumsOfLevel.getOrDefault(level, 0) + root.val);
        dfs(root.left, level + 1, sumsOfLevel);
        dfs(root.right, level + 1, sumsOfLevel);
    }
}
