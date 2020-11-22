public class CoinChange {
    // dp approach, bottom up

    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1]; // solve every previous one first
        Arrays.fill(dp, amount + 1); // amount + 1 is for empty values
        dp[0] = 0;
        for (int i = 1; i < dp.length; i++) {
            // try each coin to see if we can reduce it
            for (int coin : coins) {
                if (coin <= i)
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }

        // if the last slot is empty, then we don't have a solution
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
