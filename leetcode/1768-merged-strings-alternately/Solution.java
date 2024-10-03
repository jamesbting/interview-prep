import java.lang.StringBuilder;
class Solution {
    public String mergeAlternately(String word1, String word2) {
        final StringBuilder sb = new StringBuilder();

        int word1_ptr = 0;
        int word2_ptr = 0;
        while (word1_ptr < word1.length() || word2_ptr < word2.length()) {
            if (word1_ptr < word1.length()) {
                sb.append(word1.charAt(word1_ptr));
            }
            if (word2_ptr < word2.length()) {
                sb.append(word2.charAt(word2_ptr));
            }

            word1_ptr++;
            word2_ptr++;
        }
        return sb.toString();
    }
}