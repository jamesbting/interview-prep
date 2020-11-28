public class PairsofSongsWithTotalDurationsDivisibleby60 {
    public int numPairsDivisibleBy60(int[] time) {
        int[] remainders = new int[60];
        int count = 0;
        for (int length : time) {
            if (length % 60 == 0) {
                count += remainders[0];
            } else {
                count += remainders[60 - length % 60];
            }
            remainders[length % 60]++;
        }
        return count;
    }
}
