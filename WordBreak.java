public class WordBreak {
    public boolean wordBreak(String s, List<String> wordDict) {

        HashSet<String> set = new HashSet<>();
        for (String key : wordDict)
            set.add(key);

        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 0; i <= s.length(); i++) {
            for (int j = 0; j <= i; j++) {
                if (dp[j] && set.contains(s.substring(j, i))) {
                    System.out.println(s.substring(j, i));
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}
