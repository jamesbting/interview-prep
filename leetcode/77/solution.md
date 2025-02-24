Solution
Approach: Backtracking
Intuition

We are given thatn <= 20. Typically, problems that ask you to findallof something with low bounds can be solved with backtracking.

In backtracking, we generate all solutions one element at a time. This problem is asking us to generate all possible combinations, so we will generate combinations one element at a time.

The range of elements we are working with is[1, n]. To generate a combination one element at a time, we will use an arraycurrthat represents the current combination we are building.

To start, we add the first element1, so we havecurr = [1]. We arelockingin this1and we will now find all combinations that start with1.

To find all combinations that start with1, we start by adding the first element after1, which is2. We now havecurr = [1, 2]. We arelockingin this2and we will now find all combinations that start with1, 2.

This continues until we reach the target lengthk. Let's say that we have finished finding all combinations that start with[1, 2]. Now what? Webacktrackby removing the2, and we havecurr = [1]again. Now, we add the second element that comes after1, which is3. We havecurr = [1, 3], and now we need to find all combinations that start with[1, 3].

Once we find all the combinations that start with[1], we backtrack by removing the1fromcurrand adding the next element. We havecurr = [2], and now we need to find all combinations that start with2.

This process is very recursive in nature. Each time we add an element, we solve a new version of the problem (find all combinations that start withcurr). The initial version of the problem is to find all combinations that start with[], which represents all possible combinations.

Trees

The best way to think about the backtracking process is by modeling it as a tree. You can imagine the solution space as a tree, with each node representing a version ofcurr. Label each node with a number that represents the last number incurr. Moving to a child is like adding the child's label tocurr.

To prevent duplicate combinations like[1, 2]and[2, 1], a node only has children with labels greater than its own.

Givenn = 4andk = 2, here is the backtracking tree:



The root node represents an empty[]. From the root, every node'scurrrepresents the path taken from the root. The nodes at depthkrepresent the answer combinations (highlighted in green).

Solving this problem is equivalent to "traversing" this tree. The easiest way to perform the traversal is by using recursion and passingcurras an argument.

Think of each call to the recursive function as being a node in the tree. In each call, we need to iterate over the numbers greater than the label of the current node. We can pass an argumentfirstNumrepresenting the first number we should start iterating from.

For eachnumin[firstNum, n], we add it tocurrand then make a recursive call passingcurrandnum + 1asfirstNum. This ensures that we only consider numbers greater than the ones we have already added. Modifyingcurrand making a recursive call is equivalent to "traversing" to a child node in the tree.

When we return from a function call, it's equivalent to moving back up the tree (exactly like in a DFS). When we moved from a parent to a child, we added an element tocurr. When we move from a child back to its parent, we need to remove the element we added fromcurr. This is the "backtracking" step.

The following is an implementation of this backtrack function, which is essentially performing a DFS on the solution space tree.


An optimization step

You may notice in the solution tree image above, we have a path that does not lead to any solutions (the4node).

This path doesn't lead to any solutions because there aren't enough elements after4to reach a path length ofk. We should avoid paths like these as they are a waste of time. It would be better if our tree looked like this:



At each node, we havecurr.lengthelements so far. We need to reachkelements. Therefore, we can calculateneed = k - curr.lengthas the number of elements we still need to add.

The range of numbers we are considering in the subtree is[firstNum, n]. The size of this range isremain = n - firstNum + 1.

Finally, we can calculateavailable = remain - need. This value represents the count of numbers available to us as children. We should only consider children in the range[firstNum, firstNum + available]instead of the range[firstNum, n]like in the above code.

If we moved to a child outside of this range, likefirstNum + available + 1, then we will run out of numbers to use before reaching a length ofk.

Algorithm

Initialize an answer arrayansand an array to build combinations withcurr.
Create abacktrackfunction that takescurras an argument as well as an integerfirstNum:
ifcurr.length == k, add a copy ofcurrtoansand return.
Calculateavailable, the amount of numbers we can consider at the current node.
IteratenumfromfirstNumup to and includingfirstNum + available.
For eachnum, add it tocurr, callbacktrack(curr, num + 1), and then removenumfromcurr.
Callbacktrackwith an initially emptycurrandfirstNum = 1.
Returnans.
Implementation


Complexity Analysis

Note: most backtracking problems, including this one, have extremely difficult time complexities to derive. Don't be discouraged if you can't derive it on your own - most of the time, the analysis requires an esoteric understanding of math. If you are asked this question in an interview, do your best to state an upper bound on the complexity by analyzing the number of nodes in the tree and the work done at each node.

Time complexity:O( 
(k−1)!⋅(n−k)!
n!
​
 )

Finding combinations is awell-studied problem in combinatorics. The number of combinations of lengthkfrom a set ofnelements is equal to thebinomial coefficient, also known as "n choose k".

( 
k
n
​
 )= 
k!(n−k)!
n!
​
 

How many nodes are in the tree?

After applying the optimization, we only consider paths that lead to answers. This means that the number of leaf nodes is equal to the number of answers.

Each path to a leaf hasknodes. However, there is a huge amount of overlap. It would be extremely difficult to calculate the exact number of nodes, but we know that it can't be greater thanktimes the number of leaves (which would occur if there was no overlap, i.e. every node had a maximum of 1 child, which is only possible forn = k). Therefore, an upper bound on the number of nodes is:

k!(n−k)!
k⋅n!
​
 = 
(k−1)!⋅(n−k)!
n!
​
 

The fact that this is an upper bound is great news for us. Why? Because at each of the leaves, we need to performO(k)work to create a copy ofcurrto add to the answer. The work we perform to copy all the combinations is equal to the upper bound on the number of nodes. Therefore, the work done for the traversal will inevitably be dominated, and the fact that we can't calculate the exact number of nodes in the tree is irrelevant.

Space complexity:O(k)

We don't count the answer as part of the space complexity. The extra space we use here is forcurrand the recursion call stack. The depth of the call stack is equal to the length ofcurr, which is limited tok.

