public class ClimbingStairs {
    public int climbStairsConstantSpace(int n) {
        if (n == 1)
            return 1;
        if (n == 2)
            return 2;

        int a = 1;
        int b = 2;
        int c = a + b;
        for (int i = 2; i < n; i++) {
            int temp = b;
            c = a + b;
            a = temp;
            b = c;

        }

        return c;
    }

    public int climbStairsLinearSpace(int n) {
        if (n == 1)
            return 1;

        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < dp.length; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[dp.length - 1];
    }
}
