// https://leetcode.com/problems/remove-palindromic-subsequences/
public class removePalindromeSubsequences {
    public int removePalindromeSub(String s) {
        if(s.length() == 1 || s.length() == 0) return s.length();
        if(isPalindrome(s)) return 1; // remove the entire string
        return 2; // can always just remove all the a's then all the b's if not a palindrome itself
    }
    private boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        while(i <= j) {
            if (s.charAt(i) != s.charAt(j)) return false;
            i++;
            j--;
        }
        return true;

    }

    public int removePalindromeSubOneLine(String s) {
        return isPalindrome(s) ? Math.min(s.length, 1) : 2;
    }
}
