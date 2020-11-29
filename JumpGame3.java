import java.util.*;

public class JumpGame3 {
    public boolean canReachDFS(int[] arr, int start) {
        return helper(arr, start, 0);
    }

    private boolean helper(int[] arr, int start, int numJumps) {
        if (start < 0 || start >= arr.length || numJumps >= arr.length)
            return false;
        if (arr[start] == 0) {
            return true;
        }
        return helper(arr, start + arr[start], numJumps + 1) || helper(arr, start - arr[start], numJumps + 1);
    }

    public boolean canReachBFS(int[] arr, int start) {
        boolean[] visited = new boolean[arr.length];
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        visited[start] = true;
        while (!q.isEmpty()) {
            int curr = q.poll();
            visited[curr] = true;
            if (arr[curr] == 0)
                return true;
            if (curr - arr[curr] >= 0 && !visited[curr - arr[curr]])
                q.offer(curr - arr[curr]);

            if (curr + arr[curr] < arr.length && !visited[curr + arr[curr]])
                q.offer(curr + arr[curr]);

        }
        return false;
    }
}