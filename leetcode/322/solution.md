Solution Article
Approach 1 (Brute force) [Time Limit Exceeded]
Intuition
The problem could be modeled as the following optimization problem :
min 
x
​
 ∑ 
i=0
n−1
​
 x 
i
​
 
subject to∑ 
i=0
n−1
​
 x 
i
​
 ∗c 
i
​
 =S

, whereSis the amount,c 
i
​
 is the coin denominations,x 
i
​
 is the number of coins with denominationsc 
i
​
 used in change of amountS. We could easily see thatx 
i
​
 =[0, 
c 
i
​
 
S
​
 ].

A trivial solution is to enumerate all subsets of coin frequencies[x 
0
​
 … x 
n−1
​
 ]that satisfy the constraints above, compute their sums and return the minimum among them.

Algorithm
To apply this idea, the algorithm uses backtracking technique
to generate all combinations of coin frequencies[x 
0
​
 … x 
n−1
​
 ]
in the range([0, 
c 
i
​
 
S
​
 ])which satisfy the constraints above. It makes a sum of the combinations and returns their minimum or−1in case there is no acceptable combination.

Implementation

Complexity Analysis
Time complexity :O(S 
n
 ). In the worst case, complexity is exponential in the number of the coinsn. The reason is that every coin denominationc 
i
​
 could have at most 
c 
i
​
 
S
​
 values. Therefore the number of possible combinations is :
c 
1
​
 
S
​
 ∗ 
c 
2
​
 
S
​
 ∗ 
c 
3
​
 
S
​
 … 
c 
n
​
 
S
​
 = 
c 
1
​
 ∗c 
2
​
 ∗c 
3
​
 …c 
n
​
 
S 
n
 
​
 

Space complexity :O(n).
In the worst case the maximum depth of recursion isn. Therefore we needO(n)space used by the system recursive stack.
Approach 2 (Dynamic programming - Top down) [Accepted]
Intuition
Could we improve the exponential solution above? Definitely! The problem could be solved with polynomial time using Dynamic programming technique. First, let's define:

F(S)- minimum number of coins needed to make change for amountSusing coin denominations[c 
0
​
 …c 
n−1
​
 ]

We note that this problem has an optimal substructure property, which is the key piece in solving any Dynamic Programming problems. In other words, the optimal solution can be constructed from optimal solutions of its subproblems.
How to split the problem into subproblems? Let's assume that we knowF(S)where some changeval 
1
​
 ,val 
2
​
 ,…forSwhich is optimal and the last coin's denomination isC.
Then the following equation should be true because of optimal substructure of the problem:

F(S)=F(S−C)+1

But we don't know which is the denomination of the last coinC. We computeF(S−c 
i
​
 )for each possible denominationc 
0
​
 ,c 
1
​
 ,c 
2
​
 …c 
n−1
​
 and choose the minimum among them. The following recurrence relation holds:

F(S)=min 
i=0...n−1
​
 F(S−c 
i
​
 )+1
subject to  S−c 
i
​
 ≥0

F(S)=0 ,when S=0
F(S)=−1 ,when n=0

Recursion tree for finding coin change of amount 6 with coin denominations {1,2,3}.

In the recursion tree above, we could see that a lot of subproblems were calculated multiple times. For example the problemF(1)was calculated13times. Therefore we should cache the solutions to the subproblems in a table and access them in constant time when necessary

Algorithm
The idea of the algorithm is to build the solution of the problem from top to bottom. It applies the idea described above. It use backtracking and cut the partial solutions in the recursive tree, which doesn't lead to a viable solution. Тhis happens when we try to make a change of a coin with a value greater than the amountS. To improve time complexity we should store the solutions of the already calculated subproblems in a table.

Implementation

Complexity Analysis
Time complexity :O(S∗n). where S is the amount, n is denomination count.
In the worst case the recursive tree of the algorithm has height ofSand the algorithm solves onlySsubproblems because it caches precalculated solutions in a table. Each subproblem is computed withniterations, one by coin denomination. Therefore there isO(S∗n)time complexity.

Space complexity :O(S), whereSis the amount to change
We use extra space for the memoization table.

Approach 3 (Dynamic programming - Bottom up) [Accepted]
Algorithm
For the iterative solution, we think in bottom-up manner. Before calculatingF(i), we have to compute all minimum counts for amounts up toi. On each iterationiof the algorithmF(i)is computed asmin 
j=0…n−1
​
 F(i−c 
j
​
 )+1

Bottom-up approach using a table to build up the solution to F6.

In the example above you can see that:

F(3)
​
  
=min{F(3−c 
1
​
 ),F(3−c 
2
​
 ),F(3−c 
3
​
 )}+1
=min{F(3−1),F(3−2),F(3−3)}+1
=min{F(2),F(1),F(0)}+1
=min{1,1,0}+1
=1
​
 
Implementation

Complexity Analysis
Time complexity :O(S∗n).
On each step the algorithm finds the nextF(i)inniterations, where1≤i≤S. Therefore in total the iterations areS∗n.
Space complexity :O(S).
We use extra space for the memoization table.