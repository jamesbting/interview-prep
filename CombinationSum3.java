
//https://leetcode.com/problems/combination-sum-iii/submissions/
import java.util.ArrayList;
import java.util.List;
/* Recrusively create the combinations and check each time to see if a valid combination has been created
* If yes then add to the list, if not then remove and try the next one
*
*/

class combinationSum3Decreasing {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        helper(k, n, n, result, new ArrayList<Integer>());
        return result;
    }

    private void helper(int k, int n, int start, List<List<Integer>> result, List<Integer> list) {
        if (k == 0 && n == 0) {
            result.add(new ArrayList<Integer>(list));
        }

        if (n <= 0 || start <= 0)
            return;

        for (int i = Math.min(9, start); i > 0; i--) {
            list.add(i);
            helper(k - 1, n - i, i - 1, result, list);
            list.remove(list.size() - 1);
        }
    }
}

class combinationSum3Increasing {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        helper(k, n, 0, result, new ArrayList<Integer>());
        return result;
    }

    private void helper(int k, int n, int end, List<List<Integer>> result, List<Integer> list) {
        if (k == list.size() && n == 0) {
            result.add(new ArrayList<Integer>(list));
        }

        if (n <= 0 || end > 9)
            return;

        for (int i = Math.max(1, end); i < 10; i++) {
            list.add(i);
            helper(k, n - i, i + 1, result, list);
            list.remove(list.size() - 1);
        }
    }
}