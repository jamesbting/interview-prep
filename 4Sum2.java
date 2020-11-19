import java.util.*;
public class 4Sum2 {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        int N = A.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        //add sums of all pairs in C,D
        for(int c: C) 
            for(int d: D) 
                map.put(c+d, map.getOrDefault(c+d, 0) + 1);
            
        int res = 0;
        for(int a: A)
            for(int b: B)
                res += map.getOrDefault(-1 * (a + b), 0);
        return res;
    } 
}
