public class Carpooling {
    public boolean carPooling(int[][] trips, int capacity) {

        // use bucket sort
        int[] buckets = new int[1001];
        for (int[] trip : trips) {
            buckets[trip[1]] += trip[0];
            buckets[trip[2]] -= trip[0];
        }

        int currCapacity = 0;
        for (int bucket : buckets) {
            currCapacity += bucket;
            if (currCapacity > capacity)
                return false;
        }
        return true;
    }
}