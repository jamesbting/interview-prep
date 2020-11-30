public class TopKFrequentElements {
    public int[] topKFrequent(int[] nums, int k) {
        if (k == nums.length)
            return nums;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int n : nums)
            map.put(n, map.getOrDefault(n, 0) + 1);

        Queue<int[]> heap = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                return b[1] - a[1];
            }
        });

        for (int key : map.keySet()) {
            heap.offer(new int[] { key, map.get(key) });
        }
        int[] res = new int[k];
        for (int i = 0; i < res.length; i++) {
            res[i] = heap.poll()[0];
        }

        return res;
    }
}
