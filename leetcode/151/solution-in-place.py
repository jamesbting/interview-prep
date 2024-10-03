// Does not work

class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        
        char[] charArray = s.toCharArray();
        
        reverse(charArray, 0, charArray.length - 1);
        
        int start = 0;
        for (int end = 0; end < charArray.length; end++) {
            if (charArray[end] == ' ') {
                reverse(charArray, start, end - 1);
                start = end + 1; 
            }
        }
        
        reverse(charArray, start, charArray.length - 1);
        
        return cleanSpaces(charArray);
    }
    
    private void reverse(char[] arr, int left, int right) {
        while (left < right) {
            char temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }

    private String cleanSpaces(char[] arr) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != ' ') {
                result.append(arr[i]);
            } 
            if (arr[i] == ' ' && (i + 1 < arr.length && arr[i + 1] != ' ')) {
                result.append(' ');
            }
        }
        return result.toString();
    }
}
