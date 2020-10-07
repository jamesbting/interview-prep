class Solution {
    public int longestPalindrome(String s) {
        int[] count = new int[128];
        for(char c: s.toCharArray()) {
            count[c]++;
        }
        int longest = 0;
        for(int i: count) {
            longest += Math.floor(i/2) * 2;
            if(longest % 2 == 0 && i % 2 == 1) {
                longest++;
            }
        }
        return longest;
    }
}