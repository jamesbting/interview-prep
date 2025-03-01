Overview

This is yet another problem about Binary Tree traversals. As one would probably know, the common strategies to traverse aTreedata structure areBreadth-First Search(a.k.aBFS) andDepth-First Search(a.k.a.DFS).

The DFS strategy can be further distinguished aspreorder DFS,inorder DFSandpostorder DFS, depending on the relative order of visit among the node itself and its child nodes.

If one is not familiar with the concepts of BFS and DFS, one can find the corresponding problems on LeetCode to practice with. Also, we have an Explore card calledQueue & Stackwhere we cover boththe BFS traversalas well asthe DFS traversal.
Hence, in this article, we won't repeat ourselves on these concepts.

In the problem description, we are asked to return theverticalorder of a binary tree, which actually implies two sub-orders, where each node would have a 2-dimensional index (denoted as<column, row>)

tree in 2D coordinates

    column-wise order

    If we look at a binary treehorizontally, each node can be aligned to a specificcolumn, based on its relativeoffsetto the root node of the tree.

    Let us assume that the root node has a column index of0, then its left child node would have a column index of-1and its right child node would have a column index of+1, and so on.

    row-wise order


    Now if we put the nodes into averticaldimension, each node would be assigned to a specificrow, based on itslevel(i.e.the vertical distance to the root node).

    Let us assume that the root node has a row index of0, then both its child nodes would have the row index of1.

    Given the above definitions, we can now formulate the problem as a task to order the nodes based on the 2-dimensional coordinates that we defined above.

More specifically, the nodes should be ordered bycolumnfirst, and further the nodes on the same column should be orderedverticallybased on theirrowindices.



Approach 1: Breadth-First Search (BFS)

Intuition

With the formulation of the problem in the overview section, one of the most intuitive solutions to tackle the problem would be applying the BFS traversal, where the nodes would be visitedlevel by level.

With the BFS traversal, we naturally can guarantee the vertical order of the visits,i.e.the nodes athigherlevels (largerowvalues) would get visited later than the ones at lower levels.

However, we are still missing the horizontal order ( thecolumnorder). To ensure this order, we need to do some additional processing during the BFS traversal.

    The idea is that we keep a hash table (let's denote it ascolumnTable<key, value>), where we keep the node values grouped by thecolumnindex.

Thekeyin the hash table would be thecolumnindex, and the correspondingvaluewould be a list which contains the values of all the nodes that share the same column index.

In addition, the values in the corresponding list should be ordered by theirrowindices, which would be guaranteed by the BFS traversal as we mentioned before.

Algorithm

We elaborate on the steps to implement the above idea.

    First, we create a hash table namedcolumnTableto keep track of the results.

    As to the BFS traversal, a common code pattern would be to use aqueuedata structure to keep track of the order we need to visit nodes.
    We initialize the queue by putting the root node along with its column index value (0).

    We then run the BFS traversal with a loop consuming the elements from the queue.

    At each iteration within the BFS, we pop out an element from the queue. The element consists of anodeand its correspondingcolumnindex. If the node is not empty, we then populate thecolumnTablewith the value of the node. Subsequently, we then put its child nodes along with their respective column indices (i.e. column-1andcolumn+1) into the queue.

    At the end of the BFS traversal, we obtain a hash table that contains the desired node values grouped by theircolumnindices. For each group of values, they are further ordered by theirrowindices.

    We then sort the hash table by its keys,i.e. columnindex in ascending order. And finally we return the resultscolumn by column.

Complexity Analysis

    Time Complexity:O(NlogN)whereNis the number of nodes in the tree.

    In the first part of the algorithm, we do the BFS traversal, whose time complexity isO(N)since we traversed each node once and only once.

    In the second part, in order to return the ordered results, we then sort the obtained hash table by its keys, which could result in theO(NlogN)time complexity in the worst case scenario where the binary tree is extremely imbalanced (for instance, each node has only left child node.)

    As a result, the overall time complexity of the algorithm would beO(NlogN).

    Space Complexity:O(N)whereNis the number of nodes in the tree.

    First of all, we use a hash table to group the nodes with the same column index. The hash table consists of keys and values. In any case, the values would consumeO(N)memory. While the space for the keys could vary, in the worst case, each node has a unique column index,i.e.there would be as many keys as the values. Hence, the total space complexity for the hash table would still beO(N).

    During the BFS traversal, we use aqueuedata structure to keep track of the next nodes to visit. At any given moment, the queue would hold no more two levels of nodes. For a binary tree, the maximum number of nodes at a level would be2N+1​which is also the number of leafs in a full binary tree. As a result, in the worst case, our queue would consume at mostO(2N+1​⋅2)=O(N)space.

    Lastly, we also need some space to hold the results, which is basically a reordered hash table of sizeO(N)as we discussed before.

    To sum up, the overall space complexity of our algorithm would beO(N).



Approach 2: BFS without Sorting

Intuition

In the previous approach, it is a pity that the sorting of results overshadows the main part of the algorithm which is the BFS traversal. One might wonder if we have a way to eliminate the need for sorting. And the answer is yes.

    The key insight is that we only need to know therangeof the column index (i.e. [min_column, max_column]). Then we can simplyiteratethrough this range to generate the outputs without the need for sorting.

The above insight would work under theconditionthat there won't be any missing column index in the given range. And the condition always holds, since there won't be any broken branch in a binary tree.

Algorithm

To implement this optimization, it suffices to make some small modifications to our previous BFS approach.

During the BFS traversal, we could obtain the range of the column indices,i.e.with the variable ofmin_columnandmax_column.

At the end of the BFS traversal, we would then walk through the column range[min_column, max_column]and retrieve the results accordingly.

Current

Complexity Analysis

    Time Complexity:O(N)whereNis the number of nodes in the tree.


    Following the same analysis in the previous BFS approach, the only difference is that this time we don't need the costy sorting operation (i.e. O(NlogN)).

    Space Complexity:O(N)whereNis the number of nodes in the tree. The analysis follows the same logic as in the previous BFS approach.


Approach 3: Depth-First Search (DFS)

Intuition

Although we applied a BFS traversal in both of the previous approaches, it is not impossible to solve the problem with a DFS traversal.

    As we discussed in the overview section, once we assign a 2-dimensional index (i.e. <column, row>) for each node in the binary tree, to output the tree inverticalorder is to sort the nodes based on the 2-dimensional index, firstly bycolumnthen byrow, as shown in the following graph.

tree to table

Compared to the DFS traversal, the BFS traversal gives us a head start, since the nodes in higher rows would be visited later than the ones in the lower lows. As a result, we only need to focus on thecolumnorder.

That being said, we could simply traverse the tree in any DFS order (preorder, inorder or postorder), then we sort the resulting list strictly based on two keys<column, row>, which would give us the same results as the BFS traversal.

    An important note is that two nodes might share the same<column, row>, in the case, as stated in the problem, the order between these two nodes should be fromlefttorightas we did for BFS traversals.
    As a result, to ensure such a priority, one should make sure to visit the left child node before the right child node during the DFS traversal.

Algorithm

    Here we implement the above algorithm, with the trick that we applied in Approach 2 (BFS without sorting) where we obtained the range ofcolumnduring the traversal.

    First, we conduct a DFS traversal on the input tree. During the traversal, we would then build a similarcolumnTablewith thecolumnindex as the key and the list of(row, val)tuples as the value.

    At the end of the DFS traversal, we iterate through thecolumnTablevia the key ofcolumnindex. Accordingly, we have a list of(row, val)tuples associated with each key. We then sort this list, based on therowindex.

    After the above steps, we would then obtain a list of node values ordered firstly by itscolumnindex and then by itsrowindex, which is exactly the theverticalorder traversal of binary tree as defined in the problem.

Complexity Analysis

    Time Complexity:O(W⋅HlogH))whereWis the width of the binary tree (i.e.the number of columns in the result) andHis the height of the tree.


    In the first part of the algorithm, we traverse the tree in DFS, which results inO(N)time complexity.

    Once we build thecolumnTable, we then have to sort itcolumn by column.

    Let us assume the time complexity of the sorting algorithm to beO(KlogK)whereKis the length of the input. The maximal number of nodes in a column would be2H​whereHis the height of the tree, due to the zigzag nature of the node distribution. As a result, the upper bound of time complexity to sort a column in a binary tree would beO(2H​log2H​).

    Since we need to sortWcolumns, the total time complexity of the sorting operation would then beO(W⋅(2H​log2H​))=O(W⋅HlogH). Note that, the total number of nodesNin a tree is bounded byW⋅H,i.e. N<W⋅H. As a result, the time complexity ofO(W⋅HlogH)will dominate theO(N)of the DFS traversal in the first part.

    At the end of the DFS traversal, we have to iterate through thecolumnTablein order to retrieve the values, which will take anotherO(N)time.

    To sum up, the overall time complexity of the algorithm would beO(W⋅HlogH).

    An interesting thing to note is that in the case where the binary tree is completely imbalanced (e.g.node has only left child.), this DFS approach would have theO(N)time complexity, since the sorting takes no time on columns that contains only a single node. While the time complexity for our first BFS approach would beO(NlogN), since we have to sort theNkeys in thecolumnTable.

    Space Complexity:O(N)whereNis the number of nodes in the tree.

    We kept thecolumnTablewhich contains all the node values in the binary tree. Together with the keys, it would consumeO(N)space as we discussed in previous approaches.

    Since we apply the recursion for our DFS traversal, it would incur additional space consumption on the function call stack. In the worst case where the tree is completely imbalanced, we would have the size of call stack up toO(N).

    Finally, we have the output which contains all the values in the binary tree, thusO(N)space.

    So in total, the overall space complexity of this algorithm remainsO(N).
