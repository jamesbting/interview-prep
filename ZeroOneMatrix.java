public class ZeroOneMatrix {
    public int[][] updateMatrix(int[][] matrix) {
        int[][] res = new int[matrix.length][];
        for (int i = 0; i < matrix.length; i++) {

            res[i] = new int[matrix[0].length];
            Arrays.fill(res[i], Integer.MAX_VALUE - 2);
        }
        // first dp pass, do the row above and col to the left, if it exists
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    res[i][j] = 0;
                } else {
                    if (i > 0)
                        res[i][j] = Math.min(res[i][j], res[i - 1][j] + 1);
                    if (j > 0)
                        res[i][j] = Math.min(res[i][j], res[i][j - 1] + 1);
                }
            }
        }
        for (int i = matrix.length - 1; i >= 0; i--) {
            for (int j = matrix[0].length - 1; j >= 0; j--) {
                if (matrix[i][j] == 0) {
                    res[i][j] = 0;
                } else {
                    if (i < matrix.length - 1)
                        res[i][j] = Math.min(res[i][j], res[i + 1][j] + 1);
                    if (j < matrix[0].length - 1)
                        res[i][j] = Math.min(res[i][j], res[i][j + 1] + 1);
                }
            }
        }
        return res;
    }
}