
//https://leetcode.com/problems/backspace-string-compare/
import java.util.Stack;

public class BackSpaceStringCompare {
    /*
     * This solution takes O(M + N) time and O(1) memory. It uses 2 pointers that
     * starting from the end of the string, count the number of backspaces, and then
     * skips the appropriate number of characters
     * 
     * it then checks if the current letter of each pointer is equal, if it isn't
     * equal, then return false if they are equal continue searching, and also check
     * if either both of the pointers have letters to search in or if both are empty
     * if one is empty and the other isn't, then stop searching and return false
     */
    public boolean backspaceCompareLessMemory(String S, String T) {
        int i = S.length() - 1;
        int j = T.length() - 1;
        int skipS = 0;
        int skipT = 0;

        while (i >= 0 || j >= 0) {
            while (i >= 0) {
                if (S.charAt(i) == '#') {
                    skipS++;
                    i--;
                } else if (skipS > 0) {
                    i--;
                    skipS--;
                } else
                    break;
            }

            while (j >= 0) {
                if (T.charAt(j) == '#') {
                    skipT++;
                    j--;
                } else if (skipT > 0) {
                    j--;
                    skipT--;
                } else
                    break;
            }

            if (i >= 0 && j >= 0 && S.charAt(i) != T.charAt(j))
                return false;

            if ((i >= 0) != (j >= 0))
                return false;

            i--;
            j--;

        }
        return true;

    }

    /*
     * THis solution takes O(M + N) time and O(M + N) memory. It creates 2 stacks,
     * that contain the letters of each string. If the character that is encountered
     * is a backspace character, then pop off the stack if it contains elements
     */
    public boolean backspaceCompareMoreMemory(String S, String T) {
        return build(S).equals(build(T));
    }

    private Stack<Character> build(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c != '#') {
                stack.push(c);
            } else if (!stack.isEmpty()) {
                stack.pop();
            }
        }
        return stack;
    }
}
