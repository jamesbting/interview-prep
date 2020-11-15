public class WidestVerticalArea {
    public int maxWidthOfVerticalArea(int[][] points) {
        int maxWidth = Integer.MIN_VALUE;
        int[] xValues = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            xValues[i] = points[i][0];
        }
        Arrays.sort(xValues);
        for (int i = 1; i < xValues.length; i++)
            maxWidth = Math.max(xValues[i] - xValues[i - 1], maxWidth);
        return maxWidth;
    }
}
