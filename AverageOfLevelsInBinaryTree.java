/**
 * https://leetcode.com/problems/average-of-levels-in-binary-tree/
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
public class AverageOfLevelsInBinaryTree {
    public List<Double> averageOfLevels(TreeNode root) {
        List<List<Integer>> traversal = levelOrderTraversal(root);
        List<Double> res = new ArrayList<>();
        System.out.println(traversal);
        for(List<Integer> level : traversal) {
            res.add(average(level));
        }
        return res;
    }
    
    private double average(List<Integer> arr) {
        double sum = 0.0;
        for(int n : arr) {
            sum += n;
        }
        return sum / arr.size();
    }
    
    private List<List<Integer>> levelOrderTraversal(TreeNode root) {
        int level = 0;
        int size = 1;
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while(!queue.isEmpty()) {
            TreeNode curr = queue.poll();
            size--;
            
            if(curr.left != null) queue.offer(curr.left);
            if(curr.right != null) queue.offer(curr.right);
            
            if(level >= res.size()) {
                 res.add(new ArrayList<Integer>());
            }
            
            res.get(level).add(curr.val);
           
            if(size == 0) {
                size = queue.size();
                level++;
            }  
        }
        return res;
    }

     public List<Double> averageOfLevelsOnePass(TreeNode root) {
        int level = 0;
        int size = 1;
        int n = 1;
        double sum = 0.0;
        List<Double> res = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while(!queue.isEmpty()) {
            TreeNode curr = queue.poll();
            size--;
            
            if(curr.left != null) queue.offer(curr.left);
            if(curr.right != null) queue.offer(curr.right);
        
            
            sum += curr.val;
           
            if(size == 0) {
                res.add(sum / n);
                n = queue.size();
                size = queue.size();
                level++;
                sum = 0;
            }  
        }
        return res;
    }
}

