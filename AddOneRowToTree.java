/**
 * https://leetcode.com/problems/add-one-row-to-tree/
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
public class addOneRow {
    public TreeNode addOneRow(TreeNode root, int v, int d) {
        if(d == 1) return new TreeNode(v, root, null);
        dfs(root, v, d, 1);
        return root;
    }
    
    private void dfs(TreeNode root, int v, int depth, int curr) {
        if (root == null || curr >= depth) {
            return;
        } else if(curr == depth - 1) {
            root.left = new TreeNode(v, root.left, null);
            root.right = new TreeNode(v, null, root.right);
        } else {
            dfs(root.left, v, depth, curr+1);
            dfs(root.right, v, depth, curr+1);
        }
    }
}
/*
A binary tree as following:
      4
     / \  
    2   6 
   / \   
  1   1
 /     \ 
3       1  

v = 1
d = 3


*/