import java.util.*;

public class NaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrderBFS(Node root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null)
            return res;
        Queue<Node> q = new LinkedList<>();
        q.offer(root);
        int currLevelSize = 1;
        int currLevel = 0;
        while (!q.isEmpty()) {
            Node curr = q.poll();
            currLevelSize--;
            if (res.size() == currLevel)
                res.add(new ArrayList<>());
            res.get(currLevel).add(curr.val);
            for (Node neighbor : curr.children)
                q.offer(neighbor);

            if (currLevelSize == 0) {
                currLevelSize = q.size();
                currLevel++;
            }
        }
        return res;
    }

    public List<List<Integer>> levelOrderDFS(Node root) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(root, 0, res);
        return res;
    }

    private void dfs(Node root, int height, List<List<Integer>> res) {
        if (root == null)
            return;

        if (res.size() == height)
            res.add(new ArrayList<>());

        res.get(height).add(root.val);
        for (Node child : root.children) {
            dfs(child, height + 1, res);
        }
    }
}
