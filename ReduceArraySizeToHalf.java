public class ReduceArraySizeToHalf {
    public int minSetSize(int[] arr) {
        HashMap<Integer, Integer> count = new HashMap<>();

        for (int n : arr)
            count.put(n, count.getOrDefault(n, 0) + 1);

        List<Integer> occurrences = new ArrayList<>(count.values());
        Collections.sort(occurrences);
        int i = occurrences.size() - 1;
        int currLen = arr.length;
        int size = 0;

        while (currLen > arr.length / 2) {
            currLen -= occurrences.get(i);
            size++;
            i--;
        }
        return size;
    }

    /*
     * len = 10 -> 5 [3,3,3,3,5,5,5,2,2,7] [0,0,2,4,0,2,0,1,0,0,0] {3,2} 6 - 2 = 4
     * 
     */
}
