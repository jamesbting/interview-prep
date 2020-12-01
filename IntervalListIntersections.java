public class IntervalListIntersections {
    public int[][] intervalIntersection(int[][] A, int[][] B) {

        List<int[]> res = new ArrayList<>();
        int i = 0;
        int j = 0;

        while (i < A.length && j < B.length) {
            int start = Math.max(A[i][0], B[j][0]);
            int end = Math.min(A[i][1], B[j][1]);
            if (start <= end)
                res.add(new int[] { start, end });
            if (A[i][1] < B[j][1]) {
                i++;
            } else {
                j++;
            }
        }

        return res.toArray(new int[res.size()][]);
    }

    /*
     * aStart: 5 bEnd: A = [[0,2],[5,10],[13,23],[24,25]] B =
     * [[1,5],[8,12],[15,24],[25,26]]
     * 
     * [[1,2],]
     * 
     */
}
