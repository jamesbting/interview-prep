class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        return convertToInt(firstWord) + convertToInt(secondWord) == convertToInt(targetWord);
    }

    private int convertToInt(String word) {
        int res = 0;
        for (char c : word.toCharArray()) {
            res = res + (int)(c - 'a');
            res = res * 10;
        }
        return res;
    }
}