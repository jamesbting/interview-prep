
/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode() {} TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left
 * = left; this.right = right; } }
 */
import java.util.*;

public class MergeBinarySearchTree {
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> l1 = new ArrayList<>();
        List<Integer> l2 = new ArrayList<>();

        dfs(root1, l1);
        dfs(root2, l2);

        return merge(l1, l2);
    }

    private void dfs(TreeNode root, List<Integer> list) {
        if (root == null)
            return;

        dfs(root.left, list);
        list.add(root.val);
        dfs(root.right, list);
    }

    private List<Integer> merge(List<Integer> l1, List<Integer> l2) {
        if (l1.size() == 0)
            return l2;
        if (l2.size() == 0)
            return l1;

        List<Integer> result = new ArrayList<>();
        int p1 = 0;
        int p2 = 0;

        while (p1 < l1.size() && p2 < l2.size()) {
            int x = l1.get(p1);
            int y = l2.get(p2);
            if (x <= y) {
                result.add(x);
                p1++;
            } else {
                result.add(y);
                p2++;
            }
        }

        while (p1 < l1.size()) {
            result.add(l1.get(p1));
            p1++;
        }

        while (p2 < l2.size()) {
            result.add(l2.get(p2));
            p2++;
        }

        return result;
    }
}