class JumpGame3 {
    public boolean canReach(int[] arr, int start) {
        return helper(arr, start, 0);
    }

    private boolean helper(int[] arr, int start, int numJumps) {
        if (start < 0 || start >= arr.length || numJumps >= arr.length)
            return false;
        if (arr[start] == 0) {
            return true;
        }
        return helper(arr, start + arr[start], numJumps + 1) || helper(arr, start - arr[start], numJumps + 1);
    }
}