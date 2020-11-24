public class NumberOfIslands {
    public int numIslands(char[][] grid) {
        int counter = 0;
        for (int row = 0; row < grid.length; row++)
            for (int col = 0; col < grid[0].length; col++) {
                if (grid[row][col] == '1') {
                    dfs(grid, row, col);
                    counter++;
                }
            }
        return counter;
    }

    private void dfs(char[][] grid, int row, int col) {
        if (0 <= row && 0 <= col && row < grid.length && col < grid[0].length && grid[row][col] == '1') {
            grid[row][col] = '0';
            dfs(grid, row + 1, col);
            dfs(grid, row - 1, col);
            dfs(grid, row, col + 1);
            dfs(grid, row, col - 1);
        }
    }
}
