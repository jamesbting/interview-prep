private class MergeIntervals {
    public int[][] merge(int[][] intervals) {
        // sort intervals by starting time
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                return a[0] - b[0];
            }
        });

        ArrayList<int[]> newIntervals = new ArrayList<>();
        int start = intervals[0][0];
        int end = intervals[0][1];
        for (int[] interval : intervals) {
            // end stops before interval
            if (end < interval[0]) {
                newIntervals.add(new int[] { start, end });
                start = interval[0];
            }
            end = Math.max(end, interval[1]);
        }
        newIntervals.add(new int[] { start, end });
        return newIntervals.toArray(new int[newIntervals.size()][]);
    }
}