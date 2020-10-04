// accepted solution
// https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3480/
var RecentCounter = function () {
  this.callHistory = [] //call stack
}

/**
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function (t) {
  this.callHistory.push(t)
  var start = this.binarySearch(t - 3000)
  return start === -1
    ? this.callHistory.length - 1
    : this.callHistory.length - start
}

//binary search to find where the start of the index is
RecentCounter.prototype.binarySearch = function (key) {
  var low = 0
  var high = this.callHistory.length
  while (low < high) {
    const mid = Math.floor((low + high) / 2)
    if (this.callHistory[mid] < key) low = mid + 1
    else high = mid
  }
  return low
}

var obj = new RecentCounter()
var param_1 = obj.ping(1)
var param_2 = obj.ping(100)
var param_3 = obj.ping(3001)
var param_4 = obj.ping(3002)

console.log(`[${param_1},${param_2},${param_3},${param_4}]`)
