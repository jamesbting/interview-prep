public class CountSortedVowelStrings {
    private static final char[] vowels = { 'a', 'e', 'i', 'o', 'u' };
    private static final int empty = -1;

    public int countVowelStrings(int n) {
        HashMap<Character, int[]> dp = new HashMap<>();
        for (char c : vowels) {
            int[] arr = new int[n + 1];
            Arrays.fill(arr, -1); // -1 means empty
            dp.put(c, arr);
        }
        return count(n, 'a', dp) + count(n, 'e', dp) + count(n, 'i', dp) + count(n, 'o', dp) + count(n, 'u', dp);
    }

    private int count(int n, char c, HashMap<Character, int[]> dp) {
        if (n < 0)
            return 0;
        if (n == 1)
            return 1;
        if (dp.get(c)[n] != -1) {
            return dp.get(c)[n];
        }
        int answer = 0;
        for (char vowel : vowels) {
            if (vowel >= c) {
                answer += count(n - 1, vowel, dp);
            }
        }
        dp.get(c)[n] = answer;
        return answer;
    }
}

/*
 * n = 1 countVowelStrings(1) = 5 a, e , i , o , u n=2
 * 
 * []
 * 
 */