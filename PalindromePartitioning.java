public class PalindromePartitioning {
    List<List<String>> res = new ArrayList<>();

    public List<List<String>> partition(String s) {
        List<String> l = new ArrayList<>();
        backtrack(s, l);
        return res;
    }

    private void backtrack(String s, List<String> list) {
        if (s.length() == 0) {
            res.add(new ArrayList<>(list));
            return;
        }

        for (int i = 1; i <= s.length(); i++) {
            String substring = s.substring(0, i);
            if (isPalindrome(substring)) {
                list.add(substring);
                backtrack(s.substring(i), list);
                list.remove(list.size() - 1);
            }
        }

    }

    private boolean isPalindrome(String s) {
        int j = s.length() - 1;
        for (int i = 0; i < j; i++) {
            if (s.charAt(i) != s.charAt(j))
                return false;
            j--;
        }

        return true;
    }

    /*
     * i: 0 "a|a|b" [["a","a","b"], ["aa","b"]]
     */
}
