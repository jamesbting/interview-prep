/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
	let maxValue = Number.NEGATIVE_INFINITY
	let currMax = Number.NEGATIVE_INFINITY
	nums.forEach((n) => {
		currMax = Math.max(currMax, 0) + n
		maxValue = Math.max(currMax, maxValue)
	})

	return maxValue
}
