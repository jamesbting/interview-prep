import java.util.*;

public class SubrectangleQueries {

    private int[][] matrix;

    public SubrectangleQueries(int[][] rectangle) {
        this.matrix = new int[rectangle.length][];
        for (int i = 0; i < rectangle.length; i++) {
            this.matrix[i] = Arrays.copyOf(rectangle[i], rectangle[i].length);
        }
    }

    public void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for (int i = row1; i <= row2; i++) {
            for (int j = col1; j <= col2; j++) {
                this.matrix[i][j] = newValue;
            }
        }
    }

    public int getValue(int row, int col) {
        return this.matrix[row][col];
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries obj = new SubrectangleQueries(rectangle);
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue); int param_2 =
 * obj.getValue(row,col);
 */