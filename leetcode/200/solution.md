Video Solution
Solution
Approach #1 DFS [Accepted]

Intuition

Treat the 2d grid map as an undirected graph and there is an edge
between two horizontally or vertically adjacent nodes of value '1'.

Algorithm

Linear scan the 2d grid map, if a node contains a '1', then it is a root node
that triggers a Depth First Search. During DFS, every visited node should be
set as '0' to mark as visited node. Count the number of root nodes that trigger
DFS, this number would be the number of islands since each DFS starting at some
root identifies an island.

The algorithm can be better illustrated by the animation below:
Current

Complexity Analysis

    Time complexity : O(M×N) where M is the number of rows and
    N is the number of columns.

    Space complexity : worst case O(M×N) in case that the grid map
    is filled with lands where DFS goes by M×N deep.

Approach #2: BFS [Accepted]

Algorithm

Linear scan the 2d grid map, if a node contains a '1', then it is a root node
that triggers a Breadth First Search. Put it into a queue and set its value
as '0' to mark as visited node. Iteratively search the neighbors of enqueued
nodes until the queue becomes empty.

Complexity Analysis

    Time complexity : O(M×N) where M is the number of rows and
    N is the number of columns.

    Space complexity : O(min(M,N)) because in worst case where the
    grid is filled with lands, the size of queue can grow up to min(M,N).

Approach #3: Union Find (aka Disjoint Set) [Accepted]

Algorithm

Traverse the 2d grid map and union adjacent lands horizontally or vertically,
at the end, return the number of connected components maintained in the UnionFind
data structure.

For details regarding to Union Find, you can refer to this article.

The algorithm can be better illustrated by the animation below:
Current

Complexity Analysis

    Time complexity : O(M×N) where M is the number of rows and
    N is the number of columns. Note that Union operation takes essentially constant
    time1 when UnionFind is implemented with both path compression and union by rank.

    Space complexity : O(M×N) as required by UnionFind data structure.

Footnotes

    https://en.wikipedia.org/wiki/Disjoint-set_data_structure ↩
