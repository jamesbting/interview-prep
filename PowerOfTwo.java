//https://leetcode.com/problems/power-of-two/submissions/
//constant time solution
public class PowerOfTwo {
    public boolean isPowerOfTwo(int n) {
        if (n % 2 == 1 && n > 1)
            return false;
        double pow = Math.log(n) / Math.log(2);
        return pow - Math.floor(pow) < 0.00000001;
    }
}
