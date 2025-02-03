Video Solution

Solution
Integer Square Root
The value a we're supposed to compute could be defined as a 
2
 ≤x<(a+1) 
2
 . It is called integer square root. From a geometrical point of view, it's the side of the largest integer-side square with a surface less than x.

fig



Approach 1: Pocket Calculator Algorithm
Before going to the serious stuff, let's first have some fun and implement the algorithm used by the pocket calculators.

Usually, a pocket calculator computes well exponential functions and natural logarithms by having logarithm tables hardcoded or by other means. Hence the idea is to reduce the square root computation to these two algorithms as well

x
​
 =e 
2
1
​
 logx
 

That's some sort of cheat because of non-elementary function usage but it's how that actually works in real life.

fig

Implementation


Complexity Analysis

Time complexity: O(1).

Space complexity: O(1).



Approach 2: Binary Search
Intuition

Let's go back to the interview context. For x≥2 the square root is always smaller than x/2 and larger than 0 : 0<a<x/2. Since a is an integer, the problem goes down to the iteration over the sorted set of integer numbers. Here the binary search enters the scene.

fig

Algorithm

If x < 2, return x.

Set the left boundary to left = 2, and the right boundary to right = x / 2.

While left <= right:

Take num = (left + right) / 2 as a guess. Compute num * num and compare it with x:

If num * num > x, move the right boundary ``right = pivot - 1`

Else, if num * num < x, move the left boundary left = pivot + 1

Otherwise num * num == x, the integer square root is here, let's return it.

Return right

Implementation


Complexity Analysis

Time complexity : O(logN).

Let's compute time complexity with the help of master theorem T(N)=aT( 
b
N
​
 )+Θ(N 
d
 ). The equation represents dividing the problem up into a subproblems of size  
b
N
​
  in Θ(N 
d
 ) time. Here at step, there is only one subproblem a = 1, its size is half of the initial problem b = 2, and all this happens in a constant time d = 0. That means that log 
b
​
 a=d and hence we're dealing with case 2 that results in O(n 
log 
b
​
 a
 log 
d+1
 N) = O(logN) time complexity.

Space complexity : O(1).



Approach 3: Recursion + Bit Shifts
Intuition

Let's use recursion. Bases cases are  
x
​
 =x for x<2. Now the idea is to decrease x recursively at each step to go down to the base cases.

How to go down?

For example, let's notice that  
x
​
 =2× 
4
x
​
 
​
 , and hence square root could be computed recursively as

mySqrt(x)=2×mySqrt( 
4
x
​
 )

One could already stop here, but let's use left and right shifts, which are quite fast manipulations with bits

x<<ythat meansx×2 
y
 

x>>ythat means 
2 
y
 
x
​
 

That means one could rewrite the recursion above as

mySqrt(x)=mySqrt(x>>2)<<1

in order to speed up the computations.

Implementation


Complexity Analysis

Time complexity: O(logN).

Let's compute time complexity with the help of master theorem T(N)=aT( 
b
N
​
 )+Θ(N 
d
 ). The equation represents dividing the problem up into a subproblems of size  
b
N
​
  in Θ(N 
d
 ) time. Here at step, there is only one subproblem a = 1, its size is half of the initial problem b = 2, and all this happens in a constant time d = 0. That means that log 
b
​
 a=d and hence we're dealing with case 2 that results in O(n 
log 
b
​
 a
 log 
d+1
 N) = O(logN) time complexity.

Space complexity: O(logN) to keep the recursion stack.