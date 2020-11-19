import java.util.*;

public class KClosestPoints {
    public int[][] kClosest(int[][] points, int K) {
        if (points.length == K)
            return points;
        int[] distances = new int[points.length];
        for (int i = 0; i < points.length; i++)
            distances[i] = distanceFromOrigin(points[i]);

        Arrays.sort(distances);
        int distanceLimit = distances[K - 1];
        int j = 0;
        int[][] res = new int[K][];
        for (int i = 0; i < points.length; i++)
            if (distanceFromOrigin(points[i]) <= distanceLimit)
                res[j++] = points[i];

        return res;
    }

    private int distanceFromOrigin(int[] point) {
        return (int) (Math.pow(point[0], 2) + Math.pow(point[1], 2));
    }

}
