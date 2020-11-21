public class GetEqualSubstringsWithingBudget {
    public int equalSubstring(String s, String t, int maxCost) {
        int[] costs = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            costs[i] = Math.abs(s.charAt(i) - t.charAt(i));
        }
        int maxLength = Integer.MIN_VALUE;
        int currCost = 0;
        int start = 0;
        int end = 0;
        while (start < costs.length && end < costs.length) {
            if (currCost + costs[end] <= maxCost) {
                maxLength = Math.max(maxLength, end - start + 1);
                currCost += costs[end];
                end++;
            } else {
                currCost -= costs[start];
                start++;
            }
        }

        return maxLength;
    }

}
