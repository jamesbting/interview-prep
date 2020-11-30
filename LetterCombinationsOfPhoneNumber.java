public class LetterCombinationsOfPhoneNumber {
    HashMap<Integer, List<Character>> map = new HashMap<>();

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0)
            return new ArrayList<String>();
        map.put(1, new ArrayList<>());
        map.put(2, Arrays.asList('a', 'b', 'c'));
        map.put(2, Arrays.asList('a', 'b', 'c'));
        map.put(3, Arrays.asList('d', 'e', 'f'));
        map.put(4, Arrays.asList('g', 'h', 'i'));
        map.put(5, Arrays.asList('j', 'k', 'l'));
        map.put(6, Arrays.asList('m', 'n', 'o'));
        map.put(7, Arrays.asList('p', 'q', 'r', 's'));
        map.put(8, Arrays.asList('t', 'u', 'v'));
        map.put(9, Arrays.asList('w', 'x', 'y', 'z'));

        List<String> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        backtrack(digits, 0, res, sb);
        return res;
    }

    private void backtrack(String digits, int start, List<String> res, StringBuilder sb) {
        if (start >= digits.length()) {
            res.add(sb.toString());
            return;
        }

        int n = (digits.charAt(start) - '0');
        List<Character> letters = map.get(n);
        for (int i = 0; i < letters.size(); i++) {
            sb.append(letters.get(i));
            backtrack(digits, start + 1, res, sb);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
