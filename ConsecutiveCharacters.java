//https://leetcode.com/problems/consecutive-characters/
//track the power at each character using an array
public class ConsecutiveCharacters {

    public int maxPower(String s) {
        if (s.length() == 1)
            return 1;
        int[] power = new int[s.length()];
        power[0] = 1;
        int max = 1;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i - 1) == s.charAt(i)) {
                power[i] = power[i - 1] + 1;
                if (max < power[i])
                    max = power[i];
            } else {
                power[i] = 1;
            }
        }

        return max;
    }

}
