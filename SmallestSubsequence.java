import java.util.*;

public class SmallestSubsequence {
    public String smallestSubsequence(String s) {
        Stack<Character> stack = new Stack<>();

        // Store if letter is already in string
        boolean[] present = new boolean[26];

        // Store count of letter in string
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) {
            cnt[c - 'a']++;
        }

        for (char c : s.toCharArray()) {
            cnt[c - 'a']--;

            // If already present, skip
            if (present[c - 'a']) {
                continue;
            }

            while (!stack.isEmpty() && c < stack.peek() && cnt[stack.peek() - 'a'] > 0) {
                present[stack.pop() - 'a'] = false;
            }

            stack.push(c);
            present[c - 'a'] = true;
        }

        StringBuilder res = new StringBuilder();
        while (!stack.isEmpty()) {
            res.append(stack.pop());
        }

        return res.reverse().toString();
    }
}
