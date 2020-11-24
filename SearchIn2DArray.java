public class SearchIn2DArray {
    public boolean searchMatrix(int[][] matrix, int target) {
        // find closest row

        if (matrix.length == 0 || matrix[0].length == 0)
            return false;
        int m = matrix.length;
        int n = matrix[0].length;

        int start = 0;
        int end = m - 1;
        int rowIndex = 0;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (matrix[mid][0] == target || matrix[mid][n - 1] == target)
                return true;
            if (matrix[mid][0] < target && target < matrix[mid][n - 1]) {
                rowIndex = mid;
                break;
            } else if (matrix[mid][0] > target && matrix[mid][n - 1] > target) {
                end = mid - 1;
            } else if (matrix[mid][0] < target && matrix[mid][n - 1] < target) {
                start = mid + 1;
            }
        }

        start = 0;
        end = n - 1;
        int[] row = matrix[rowIndex];
        while (start <= end) {
            int mid = (start + end) / 2;
            if (row[mid] == target)
                return true;
            else if (row[mid] > target)
                end = mid - 1;
            else if (row[mid] < target)
                start = mid + 1;
        }

        return false;
    }
}