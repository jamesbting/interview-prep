Solution Article
Approach 1: Depth-first Search

Because the input is nested, it is natural to think about the problem in a recursive way. We go through the list of nested integers one by one, keeping track of the current depth d. If a nested integer is an integer, n, we calculate its sum as n×d. If the nested integer is a list, we calculate the sum of this list recursively using the same process but with depth equals d+1.

Implementation

Complexity Analysis

Let N be the total number of nested elements in the input list. For example, the list [ [[[[1]]]], 2 ] contains 4 nested lists and 2 nested integers (1 and 2), so N=6 for that particular case.

    Time complexity : O(N).

    Recursive functions can be a bit tricky to analyze, particularly when their implementation includes a loop. A good strategy is to start by determining how many times the recursive function is called, and then how many times the loop will iterate across all calls to the recursive function.

    The recursive function, dfs(...) is called exactly once for each nested list. As N also includes nested integers, we know that the number of recursive calls has to be less than N.

    On each nested list, it iterates over all of the nested elements directly inside that list (in other words, not nested further). As each nested element can only be directly inside one list, we know that there must only be one loop iteration for each nested element. This is a total of N loop iterations.

    So combined, we are performing at most 2⋅N recursive calls and loop iterations. We drop the 2 as it is a constant, leaving us with time complexity O(N).

    Space complexity : O(N).

    In terms of space, at most O(D) recursive calls are placed on the stack, where D is the maximum level of nesting in the input. For example, D=2 for the input [[1,1],2,[1,1]], and D=3 for the input [1,[4,[6]]].

    In the worst case, D=N, (e.g. the list [[[[[[]]]]]]) so the worst-case space complexity is O(N).


Approach 2: Breadth-first Search

We can also solve the problem using a breadth-first search. The algorithm for this is closely based on the standard breadth-first search template. The algorithm fully processes each depth before moving to the next one.

Implementation

Complexity Analysis

    Time complexity : O(N).

    Similar to the DFS approach. Each nested element is put on the queue and removed from the queue exactly once.

    Space complexity : O(N).

    The worst-case for space complexity in BFS occurs where most of the elements are in a single layer, for example, a flat list such as [1, 2, 3, 4, 5] as all of the elements must be put on the queue at the same time. Therefore, this approach also has a worst-case space complexity of O(N).
