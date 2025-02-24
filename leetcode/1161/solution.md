Solution
Overview
We are given therootof a binary tree.

Our task is to return the smallest levelxsuch that the sum of all the values of nodes at levelxis maximal.

Approach 1: Breadth First Search
Intuition
The task is to compute the sum of all node values at each level to get the smallest level with the maximum sum.

We can simply use a standard breadth-first search traversal because we need to analyze nodes by level.

BFS is an algorithm for traversing or searching a graph. It traverses in a level-wise manner, i.e., all the nodes at the present level (sayl) are explored before moving on to the nodes at the next level (l + 1). BFS is implemented with a queue.

Here is an example with the steps:

img

If you are not familiar with BFS traversal, we suggest you read ourLeetCode Explore Card.

We initialize a queue of integers and an integerlevel = 0to track the current level. In the queue, we push therootnode.

We perform a level-wise traversal, incrementinglevelby1each time when we move to a new level. At each iteration, we remove all nodes atlevel, compute the sum of all node values at this level, and insert all their neighbouring nodes atlevel + 1.

Because we are popping all of the nodes atleveland inserting all of the nodes atlevel + 1, the size of the queue will represent the number of nodes at the next level at the end of this iteration.

So we have two loops: the outer loop runs until the queue is empty, and the inner loop runs the number of times equal to the size of the queue to just cover the nodes at the current level. We will pop all the nodes atlevel, compute the sum of all the values, and insert all the nodes atlevel + 1into the queue.

Here is a visual representation of how we will iterate using the loops:

img

To get the answer, we compare the sum of all node values at the current level to the maximum sum of values we've already seen. If the current sum of node values is greater than what we've seen before, we update our answer tolevel, and the current sum becomes our largest sum of values seen thus far. Since we are traversing the higher levels first, by only updating the answer when the level sum isgreaterthan what we've seen before, we handle the tiebreakers automatically.

Algorithm
Create an integer variablemaxSumto keep track of the maximum sum of node values at any level. We start with a large negative value.
Create another variableansto store the answer to the problem.
Create another integer variablelevelto store the current level through which we are iterating. We initialize it with0.
Initialize a queueqofTreeNodeand pushrootinto it.
Perform a BFS traversal until the queue is empty:
Incrementlevelby1and initializesumAtCurrentLevel = 0to compute the sum of all values of nodes at this level.
Iterate through all the nodes atlevelusing only theq.size()number of nodes. Within this inner loop, pop out all the nodes at the current level one by one, adding their values tosumAtCurrentLeveland pushing the left and right children (if they exist) into the queue.
Realize that after traversing all of the nodes atlevel, the queue only has nodes atlevel + 1.
After traversing through all the nodes atlevel, we check ifsumAtCurrentLevelis greater thanmaxSum. IfmaxSum < sumAtCurrentLevel, update our answer variable toans = leveland setmaxSum = sumAtCurrentLevel.
Returnans.
Implementation

Complexity Analysis
Herenis the number of nodes in the given binary tree.

Time complexity:O(n).

Each queue operation in the BFS algorithm takesO(1)time, and a single node can only be pushed once, leading toO(n)operations fornnodes.
The computation of sum of all the values of nodes at a level also takesO(n)time as each node's value is used once.
Space complexity:O(n).

As the BFS queue stores the nodes in level-wise manner, the maximum number of nodes in the BFS queue would equal to the most number of nodes at any level. So, the best case would beO(1)where all the levels have just one node.
The worst case would be a complete binary tree. In a complete binary tree, the last or second last level would have the most nodes (the last level can have multiple null nodes). Because we are iterating by level, the BFS queue will be most crowded when all of the nodes from the last level (or second last level) are in the queue. Assume we have a complete binary tree with heighthand a fully filled last level having2 
h
 nodes. All the nodes at each level add up to1+2+4+8+...+2 
h
 =n. This implies that2 
h+1
 −1=n, and thus2 
h
 =(n+1)/2. Because the last levelhhas2 
h
 nodes, the BFS queue will have(n+1)/2=O(n)elements in the worst-case scenario.
Approach 2: Depth First Search
Intuition
We can also use another traversal method, depth-first search (DFS).

In DFS, we use a recursive function to explore nodes as far as possible along each branch. Upon reaching the end of a branch, we backtrack to the next branch and continue exploring.

Once we encounter an unvisited node, we will take one of its neighbor nodes (if exists) as the next node on this branch. Recursively call the function to take the next node as the 'starting node' and solve the subproblem.

img

If you are new to Depth First Search, please see ourLeetCode Explore Cardfor more information on it!

Because our task is to compute the sum of all the values of nodes at each level, we can perform a DFS traversal and pass the level of each node as an extra parameter.

We can initialize a list of integerssumOfNodesAtLevel, wheresumOfNodesAtLevel[i]stores the sum of all the values of nodes at leveli. Whenever we visit a node at a level, sayl, we increment the indexlin the list by the value of the current node. According to the problem definition, the levels should begin with1, but to keep the list as0-indexed, we will begin with level0(the root's level) and increment our answer by1at the end.

The question that may arise is how long this list should be.

We know that in a DFS traversal, we either move down the tree (until we can) to a node at the next level or we backtrack to a node at a lower level. As we descend the tree, if we come across a levellwe haven't seen before, we add the node's value tosumOfNodesAtLevel, which places the entry at indexlitself. This is due to the fact that all levels from0tol - 1must have already been seen and have corresponding values insumOfNodesAtLevel.

So, if the size ofsumOfNodesAtLevelequalsl, it means we've seen nodes from levels0tol - 1but not any nodes at levellyet. At levell, this is the first node we see.

If the levellis smaller than the size ofsumOfNodesAtLevel, it means we've seen some nodes at this level before, and we simply incrementsumOfNodesAtLevel[l]by the value of the current node.

Algorithm
Create a list of integerssumOfNodesAtLevelto store the sum of all the values of nodes at a level. The valuesumOfNodesAtLevel[i]stores the sum of all the values of nodes at leveli(0-indexed). We would start our levels from0to keep the array0-indexedand finally increment our answer by1to align with the problem definition of the level (levels begin with1as stated in the problem).
Perform the DFS traversal over the given binary tree. We calldfs(root, 0, sumOfNodesAtLevel)wheredfsis a recursive method that takes three parameters:TreeNode nodefrom which the traversal begins, the level ofnode, andsumOfNodesAtLevel. We perform the following in this method:
Ifnodeisnull, return.
If the size ofsumOfNodesAtLevelequalslevel, we haven't encountered any nodes at this level. Hence, we insertnode.valinsumOfNodesAtLevel. Otherwise, if we've seen this level before, we simply performsumOfNodesAtLevel[level] += node.valto addnode.valto the correspondinglevel.
Recursively perform DFS fromnode.left.
Recursively perform DFS fromnode.right.
Create a variablemaxSumto keep track of the maximum sum of node values at any level. We start with a large negative value.
Create another variableansto store the answer to the problem.
Iterate over the sum of nodes of all the levels, i.e., iterate oversumOfNodesAtLeveland perform the following:
IfmaxSum < sumOfNodesAtLevel[i], we setmaxSum = sumOfNodesAtLevel[i]and updateansto the leveli + 1(+1is added to align with the definition of level).
Returnans.
Implementation

Complexity Analysis
Herenis the number of nodes in the given binary tree.

Time complexity:O(n).

We traverse once over each node of the tree using DFS traversal which takesO(n)time. We also takeO(1)time to add a node's value intosumOfNodesAtLevelfor each node, which takesO(n)time fornnodes.
The size ofsumOfNodesAtLevelis equal to the height of tree. We iterate over all the values insumOfNodesAtLevelto get the level with maximum sum of node values. In the worst-case scenario, when the tree is a straight line, the height would beO(n), requiringO(n)time to iterate oversumOfNodesAtLevel.
Space complexity:O(n).

The DFS traversal is recursive and would take some space to store the stack calls. The maximum number of active stack calls at a time would be the tree's height, which in the worst case would beO(n)when the tree is a straight line.
ThesumOfNodesAtLevelwould also take linear space in the worst case.