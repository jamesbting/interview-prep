Solution
Approach 1: One Pass

Intuition

The problem is known as Dutch National Flag Problem and first was proposed by Edsger W. Dijkstra. The idea is to attribute a color to each number and then arrange them following the order of colors on the Dutch flag.

bla

Let's use a three-pointer to track the rightmost boundary of zeros, the leftmost boundary of twos, and the current element under consideration.

bla

The idea of a solution is to move curr pointer along the array, if nums[curr] = 0 - swap it with nums[p0], if nums[curr] = 2 - swap it with nums[p2].

Algorithm

    Initialise the rightmost boundary of zeros: p0 = 0. During the algorithm execution nums[idx < p0] = 0.

    Initialise the leftmost boundary of twos: p2 = n - 1. During the algorithm execution nums[idx > p2] = 2.

    Initialise the index of the current element to consider: curr = 0.

    While curr <= p2 :

        If nums[curr] = 0: swap currth and p0th elements and move both pointers to the right.

        If nums[curr] = 2: swap currth and p2th elements. Move pointer p2 to the left.

        If nums[curr] = 1: move pointer curr to the right.

Implementation

Current

Complexity Analysis

    Time complexity : O(N) since it's one pass along the array of length N.

    Space complexity : O(1) since it's a constant space solution.
