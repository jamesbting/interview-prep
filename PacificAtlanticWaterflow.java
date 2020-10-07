
//DFS problem
//https://leetcode.com/problems/pacific-atlantic-water-flow/
//Make 2 boolean matrices, and set to true if water can flow. If the element at i,j for the pacific ocean and the atlantic ocean are true, then add to (i,j) list
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class PacificAtlanticWaterflow {
    static int[] dX = { -1, 1, 0, 0 };
    static int[] dY = { 0, 0, 1, -1 };

    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        List<List<Integer>> res = new ArrayList<>();

        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return res;
        int m = matrix.length;
        int n = matrix[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];

        // first column of pacific and last column of atlantic set to true
        for (int i = 0; i < m; i++) {
            pacific[i][0] = true;
            atlantic[i][n - 1] = true;
        }

        // first row of pacific and last row of atlantic to true
        for (int j = 0; j < n; j++) {
            pacific[0][j] = true;
            atlantic[m - 1][j] = true;
        }

        // DFS on the first column of pacific, and the last column of atlantic
        for (int i = 0; i < m; i++) {
            explore(pacific, matrix, i, 0);
            explore(atlantic, matrix, i, n - 1);
        }

        // DFS on the row of pacific and the last row of atlantic
        for (int j = 0; j < n; j++) {
            explore(pacific, matrix, 0, j);
            explore(atlantic, matrix, m - 1, j);

        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }
        return res;
    }

    private void explore(boolean[][] grid, int[][] matrix, int i, int j) {
        grid[i][j] = true;
        for (int d = 0; d < dX.length; d++) {
            if (i + dY[d] < grid.length && i + dY[d] >= 0 && j + dX[d] < grid[0].length && j + dX[d] >= 0) {
                if (!grid[i + dY[d]][j + dX[d]] && matrix[i + dY[d]][j + dX[d]] >= matrix[i][j]) {
                    explore(grid, matrix, i + dY[d], j + dX[d]);
                }
            }
        }
    }
}