import java.util.ArrayList;
import java.util.List;

class combinationSum3 {
    public List<List<Integer>> combinationSum3Decreasing(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        helperDecreasing(k, n, n, result, new ArrayList<Integer>());
        return result;
    }

    private void helperDecreasing(int k, int n, int start, List<List<Integer>> result, List<Integer> list) {
        if (k == 0 && n == 0) {
            result.add(new ArrayList<Integer>(list));
        }

        if (n <= 0 || start <= 0)
            return;

        for (int i = Math.min(9, start); i > 0; i--) {
            list.add(i);
            helperDecreasing(k - 1, n - i, i - 1, result, list);
            list.remove(list.size() - 1);
        }
    }
}