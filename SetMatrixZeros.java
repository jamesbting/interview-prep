public class SetMatrixZeros {
    public void setZeroes(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        boolean firstCol = false;
        // set first element in row and col to zero if we need to set to zero
        for (int row = 0; row < n; row++) {
            if (matrix[row][0] == 0)
                firstCol = true;
            for (int col = 1; col < m; col++) {
                if (matrix[row][col] == 0) {
                    matrix[row][0] = 0;
                    matrix[0][col] = 0;
                }
            }
        }

        // update all rows and cols
        for (int row = 1; row < n; row++) {
            for (int col = 1; col < m; col++) {
                if (matrix[row][0] == 0 || matrix[0][col] == 0)
                    matrix[row][col] = 0;
            }
        }

        // if 0,0 is zero, then set the first row to zero
        if (matrix[0][0] == 0)
            for (int i = 0; i < m; i++)
                matrix[0][i] = 0;

        if (firstCol)
            for (int i = 0; i < n; i++)
                matrix[i][0] = 0;
    }
}
