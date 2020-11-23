import java.util.*;

public class CombinationSum2 {

    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        dfs(candidates, target, 0, 0, new ArrayList<Integer>());
        return res;
    }

    private void dfs(int[] candidates, int target, int sum, int start, List<Integer> combination) {
        if (target == sum) {
            res.add(new ArrayList<>(combination));
            return;
        }
        if (target < sum)
            return;

        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i - 1])
                continue;
            int candidate = candidates[i];
            combination.add(candidate);
            dfs(candidates, target, sum + candidate, i + 1, combination);
            combination.remove(combination.size() - 1);
        }
    }
}
