// https://leetcode.com/problems/distribute-candies/

public class DistributeCandies {
    public int distributeCandies(int[] candyType) {
        HashSet<Integer> set = new HashSet<>();
        
        for (int candy : candyType) {
            set.add(candy);
        }
        return Math.min(candyType.length / 2, set.size());

        
    }
}