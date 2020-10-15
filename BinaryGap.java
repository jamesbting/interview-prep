class BinaryGap {
    public int binaryGapSlidingWindow(int n) {
        String binary = Integer.toBinaryString(n);
        int fast = 0;
        int slow = 0;
        int maxDistance = Integer.MIN_VALUE;
        while (fast < binary.length() && slow < binary.length()) {
            if (binary.charAt(fast) == '1') {
                maxDistance = Math.max(maxDistance, fast - slow);
                slow = fast;
            }
            fast++;
        }
        return maxDistance;
    }

    public int binaryGapDivision(int n) {
        int[] oddBits = new int[32];
        int j = 0;
        for (int i = 0; i < 32 && n > 0; i++) {
            if (n % 2 == 1) {
                oddBits[j++] = i;
            }
            n /= 2;
        }
        int maxDistance = 0;
        for (int k = 1; k < oddBits.length; k++) {
            maxDistance = Math.max(maxDistance, oddBits[k] - oddBits[k - 1]);
        }
        return maxDistance;
    }
}