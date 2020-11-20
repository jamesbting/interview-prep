public class FlipAndInvertImage {
    public int[][] flipAndInvertImage(int[][] A) {
        int[][] newImage = new int[A.length][];
        for (int i = 0; i < A.length; i++) {
            newImage[i] = new int[A[0].length];
            for (int j = A[0].length - 1; j >= 0; j--)
                newImage[i][A[0].length - 1 - j] = A[i][j] == 1 ? 0 : 1;
        }

        return newImage;
    }
}