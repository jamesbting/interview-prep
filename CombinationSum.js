//accepted solution
// https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3481/

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  var output = []
  generateCombinations(candidates, target, 0, 0, output, [])
  return output
}

function generateCombinations(candidates, target, start, sum, output, list) {
  if (sum > target) return

  if (sum === target) {
    output.push([...list])
    return
  }
  for (var i = start; i < candidates.length; i++) {
    list.push(candidates[i])
    generateCombinations(
      candidates,
      target,
      i,
      sum + candidates[i],
      output,
      list
    )
    list.pop()
  }
}
