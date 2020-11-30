
//DFS problem
//https://leetcode.com/problems/pacific-atlantic-water-flow/
//Make 2 boolean matrices, and set to true if water can flow. If the element at i,j for the pacific ocean and the atlantic ocean are true, then add to (i,j) list
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class PacificAtlanticWaterflow {
    class Solution {
        private static int[][] dir = { { -1, 0 }, { 1, 0 }, { 0, 1 }, { 0, -1 } };

        public List<List<Integer>> pacificAtlantic(int[][] matrix) {
            int m = matrix.length;
            int n = m == 0 ? 0 : matrix[0].length;
            boolean[][] pacific = new boolean[m][n];
            boolean[][] atlantic = new boolean[m][n];

            for (int i = 0; i < n; i++) {
                dfs(matrix, 0, i, pacific);
                dfs(matrix, m - 1, i, atlantic);
            }

            for (int i = 0; i < m; i++) {
                dfs(matrix, i, 0, pacific);
                dfs(matrix, i, n - 1, atlantic);
            }

            List<List<Integer>> res = new ArrayList<>();
            for (int i = 0; i < m; i++)
                for (int j = 0; j < n; j++)
                    if (pacific[i][j] && atlantic[i][j])
                        res.add(Arrays.asList(i, j));

            return res;
        }

        private void dfs(int[][] matrix, int row, int col, boolean[][] visited) {
            visited[row][col] = true;
            for (int[] delta : dir) {
                int x = row + delta[0];
                int y = col + delta[1];
                if (isValid(x, y, visited) && matrix[row][col] <= matrix[x][y]) {
                    dfs(matrix, x, y, visited);
                }
            }
        }

        private boolean isValid(int row, int col, boolean[][] visited) {
            return 0 <= row && row < visited.length && 0 <= col && col < visited[0].length && !visited[row][col];
        }
    }

    /*
     * Pacific ~ ~ ~ ~ ~ ~ 1 2 2 3 (5) * ~ 3 2 3 (4) (4) * ~ 2 4 (5) 3 1 * ~ (6) (7)
     * 1 4 5 * ~ (5) 1 1 2 4 * * * * * Atlantic [[f,f,f,f,f],[],[],[],[]]
     * 
     * 
     */
}