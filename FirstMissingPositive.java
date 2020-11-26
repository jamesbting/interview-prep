import java.util.*;

public class FirstMissingPositive {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums);

        int firstPositive = 0;
        while (firstPositive < nums.length && nums[firstPositive] <= 0)
            firstPositive++;
        if (firstPositive == nums.length || nums[firstPositive] != 1)
            return 1;

        int smallestPositive = 1;

        for (int i = firstPositive + 1; i < nums.length; i++) {
            while (i < nums.length && nums[i - 1] == nums[i])
                i++;
            if (i == nums.length || nums[i] > smallestPositive + 1)
                return smallestPositive + 1;
            smallestPositive++;

        }

        return smallestPositive + 1;
    }

    public int firstMissingPositiveLinear(int[] nums) {

        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int n : nums) {
            if (n > 0)
                heap.offer(n);
        }

        int smallestPositive = 1;

        while (!heap.isEmpty()) {
            if (heap.peek() != smallestPositive) {
                return smallestPositive;
            }
            int last = heap.poll();
            while (!heap.isEmpty() && heap.peek() == last)
                heap.poll();
            smallestPositive++;
        }
        return smallestPositive;
    }
}
