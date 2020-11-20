import java.util.*;

public class BuildBalanced {
    /**
     * Definition for a binary tree node. public class TreeNode { int val; TreeNode
     * left; TreeNode right; TreeNode() {} TreeNode(int val) { this.val = val; }
     * TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left
     * = left; this.right = right; } }
     */
    public TreeNode balanceBST(TreeNode root) {
        List<Integer> sorted = new ArrayList<>();
        getSorted(root, sorted);
        TreeNode balanced = new TreeNode();
        buildBalanced(balanced, sorted, 0, sorted.size() - 1);
        return balanced;
    }

    private void buildBalanced(TreeNode root, List<Integer> sorted, int start, int end) {
        if (start > end)
            return;
        int mid = (start + end) / 2;
        root.val = sorted.get(mid);
        if (start <= mid - 1) {
            root.left = new TreeNode();
            buildBalanced(root.left, sorted, start, mid - 1);
        }

        if (mid + 1 <= end) {
            root.right = new TreeNode();
            buildBalanced(root.right, sorted, mid + 1, end);
        }

    }

    private void getSorted(TreeNode root, List<Integer> sorted) {
        if (root == null)
            return;

        getSorted(root.left, sorted);
        sorted.add(root.val);
        getSorted(root.right, sorted);
    }
}
