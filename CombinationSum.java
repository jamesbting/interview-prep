public class CombinationSum {

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        dfs(graph, res, path, 0);
        return res;
    }

    private void dfs(int[][] graph, List<List<Integer>> res, List<Integer> path, int currNode) {
        // base case

        if (currNode == graph.length - 1) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int neighbour : graph[currNode]) {
            path.add(neighbour);
            dfs(graph, res, path, neighbour);
            path.remove(path.size() - 1);
        }
    }
}
