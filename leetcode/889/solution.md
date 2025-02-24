Solution
Overview

We are given two integer arrays that represent thepreorderandpostordertraversals of a binary tree. Our task is to rebuild the tree and return its root. First, let's clarify the key terms involved in this task:

Abinary treeis a tree data structure where each node has at most two children, calledleftandright. Tree traversal means visiting all the nodes in a specific order. In this problem, we use two common types of binary tree traversal:

    Preorder traversal: We visit the current node first, then go to the left child, and finally to the right child. This means that the parent node will appear before its children in thepreorderarray.

Current

    Postorder traversal: We temporarily ignore the current node and move directly to its children, visiting the left child first and then the right. After that, we return to the node and process it last. In other words, the parent node always appears after its children in thepostorderarray.

Current

    For a more comprehensive understanding of binary trees, check out theBinary Tree Explore Card 🔗. This resource provides an in-depth look at binary trees, explaining their key concepts and applications with a variety of problems to solidify understanding of the pattern.

If you'd like more practice with binary trees, you can first try to construct the two traversals that we are going to use in this problem:

    Binary Tree Preorder Traversal
    Binary Tree Postorder Traversal

Approach 1: Divide and Conquer
Intuition

Binary trees are inherently recursive structures, meaning we can break them down into smaller subtrees until the problem becomes simple enough to solve directly. In this problem, the base cases are straightforward: if the traversal arrays contain only one element, the tree consists of a single node with that element as its value. Even simpler, when the arrays are empty, the tree isNULL.

For cases where the arrays contain more than one element, we assume we already know how to solve the problem for smaller trees (N−1elements or fewer). The key observation is that the first node in the preorder traversal is always the root of the tree. Our goal, then, is to correctly determine which parts of the preorder and postorder arrays correspond to the left and right subtrees. Once we identify these sections, we can recursively construct the left and right subtrees and attach them to the root, forming the complete tree.

To determine which nodes belong to the left and right subtrees, note that the second element in the preorder array is the root of the left subtree, which we'll callleftRoot. In thepostorderarray, all nodes visited beforeleftRootbelong to the left subtree. Conversely, the nodes visited afterleftRootin thepostorderarray belong to the right subtree. Using this division, we can pass the appropriate segments of the arrays to the recursive function, allowing it to build the tree step by step.

This approach is based on theDivide and Conquertechnique, where we recursively break the problem down into two or more subproblems of the same type, continuing until we reach a base case. For a deeper understanding of the topic, you can refer to the relevantLeetCode Explore Card 🔗.
Algorithm

    Define the recursive functionconstructTree(preStart, preEnd, postStart, preorder, postorder):
        IfpreStart > preEnd, i.e. there are no more nodes to process, returnNULL.
        IfpreStart == preEnd, the tree contains only one node:
            Return a new node with valuepreorder[preStart]and no children.
        DefineleftRootas the second element of the current portion of the preorder array, i.e.,preorder[preStart + 1].
        InitializenumOfNodesInLeftto1.
        Iterate over the current portion of thepostorderarray untilleftRootis found. Whilepostorder[postStart + numOfNodesInLeft - 1] != leftRoot:
            IncrementnumOfNodesInLeftby1.
        Create a new noderootand set its value topreorder[preStart].
        Recursively construct the left subtree of root by callingconstructTree(preStart + 1, preStart + numOfNodesInLeft, postStart, preorder, postorder).
        Construct the right subtree by calling:constructTree(preStart + numOfNodesInLeft + 1, preEnd, postStart + numOfNodesInLeft, preorder, postorder).
        Returnroot.
    In the mainconstructFromPrePostfunction:
        InitializenumOfNodesto the size of the traversal arrays.
        Call the helper functionconstructTree(preStart = 0, preEnd = numOfNodes - 1, postStart = 0, preorder, postorder)and return the root of the constructed tree.

Implementation
Complexity Analysis

Letnbe the size of the traversal arrays.

    Time complexity:O(n2)

    We call theconstructTreefunctionntimes, once for each element in the preorder array. In each call, the function makes a linear pass over thepostorderarray to find the position of the element that matches the root of the left subtree. This means each call toconstructTreetakesO(n)time, and withncalls in total, the overall time complexity isO(n2).

    Space complexity:O(n)

    Since we are not using any additional data structures other than the input arrays and the result tree, the space complexity is determined by the depth of the recursion. In the worst case, where the tree is a list of nodes with only left children, the recursion will goO(n)levels deep, one for each node. Therefore, the algorithm requiresO(n)extra space.

Approach 2: Using Index Array
Intuition

Looking at our previous approach, we see that searching through thepostorderarray in each call toconstructTreeadds an extraO(n)time cost, slowing down the algorithm. How can we remove this bottleneck while using the fact that all node values are unique?

An intuitive solution might be to use a hash map to store the index of each node value inpostorder. This allows quick lookups and helps us determine how many nodes belong to each subtree efficiently. While this works well and keeps the time and space complexity the same, we can optimize further. Since node values do not exceed the length of the traversal arrays, we can use an index array instead of a hash map. This improves both runtime and auxiliary space usage.

So, in the preprocessing phase, we create an index array by storing the position of each element in the post-order traversal. This index array replaces the need for the original post-order array in recursion.

The algorithm then follows the same structure: the first node in the current preorder segment is the root, and the second is the root of its left subtree (leftRoot). By finding the index ofleftRootin post-order, we determine the left subtree's size and split the problem into two smaller subproblems. We then recursively build the left and right subtrees using the relevant subarrays.
Algorithm

    Define the recursive functionconstructTree(preStart, preEnd, postStart, preorder, indexInPostorder):
        IfpreStart > preEnd, meaning that there are no more nodes to process, returnNULL.
        IfpreStart == preEnd, the tree contains only one node:
            Return a new node with valuepreorder[preStart]and no children.
        DefineleftRootas the second element of the current portion of the preorder array, i.e.,preorder[preStart + 1].
        InitializenumOfNodesInLefttoindexInPostorder[leftRoot] - postStart + 1, indicating the number of nodes that occur beforeleftRootinpostorderand should be added to the left subtree.
        Create a new noderootand set its value topreorder[preStart].
        Recursively construct the left subtree ofrootby calling:constructTree(preStart + 1, preStart + numOfNodesLeft, postStart, preorder, indexInPostorder).
        Construct the right subtree by calling:constructTree(preStart + numOfNodesInLeft + 1, preEnd, postStart + numOfNodesInLeft, preorder, indexInPostorder).
        Returnroot.
    In the mainconstructFromPrePostfunction:
        InitializenumOfNodesto the size of the traversal arrays.
        Create an index arrayindexInPostorderof sizenumOfNodes + 1.
        Iterate overpostorderand for each element store its index in theindexInPostorderarray.
        Call the helper functionconstructTree(preStart = 0, preEnd = numOfNodes - 1, postStart = 0, preorder, indexInPostorder)and return the root of the constructed tree.

Implementation
Complexity Analysis

Letnbe the size of the traversal arrays.

    Time complexity:O(n)

    TheconstructTreefunction is called exactlyntimes, once for each node in the tree. Unlike the previous approach, each call handles a constant amount of work because subtree sizes are computed in constant time using theindexInPostorderarray. As a result, the overall time complexity remainsO(n).

    Space complexity:O(n)

    TheindexInPostorderarray requiresO(n)space, as it stores the index of each element in thepostordertraversal. Additionally, in the worst case, the recursion depth can reachnlevels, leading to a total space complexity ofO(n)for both recursion and auxiliary data structures.

Approach 3: Optimized Recursion
Intuition

In the previous approaches, we explicitly searched for the dividing point between the left and right subtrees usingpostorder, which introduced an additional lookup step. Here we remove that extra search by dynamically determining subtree boundaries as we traverse the arrays, making the recursion more efficient.

The core idea is to process nodes in preorder to determine which nodes to create and use postorder to recognize when a subtree is complete. Since preorder always visits nodes in the order Root → Left → Right, each recursive call picks the next node frompreorderand assigns it as the root of the current subtree. Meanwhile, since postorder follows Left → Right → Root, a subtree is fully processed when we encounter its root inpostorder. To track this, we maintain an indexposIndexthat moves forward as nodes get finalized.

To construct the tree, we first check if the current root’s value matchespostorder[posIndex]. If it does, the subtree ends at this node, meaning it has no children. Otherwise, we attempt to construct the left subtree by making a recursive call. If the next value still doesn’t matchpostorder[posIndex], it means there must also be a right subtree, so we make another recursive call to construct it.

Once both subtrees are built, we moveposIndexforward to mark this node and its subtree as fully processed.
Algorithm

    Define the recursive functionconstructTree(preIndex, postIndex, preorder, postorder):
        Create a new noderootwith valuepreorder[preIndex].
        IncrementpreIndexby1to mark this node as created.
        If the value of root is not equal topostorder[postIndex], meaning that the node has children:
            Recursively construct the left subtree using:constructTree(preIndex, postIndex, preorder, postorder).
        If the value ofrootis still not equal topostorder[postIndex], the node has a right child as well:
            Construct the right subtree using:constructTree(preIndex, postIndex, preorder, postorder).
        IncrementpostIndexby1to mark this node and its subtree as processed.
        Returnroot.
    In the mainconstructFromPrePostfunction:
        Initialize two variables,preIndex = 0,postIndex = 0.
        Create the tree usingconstructTree(preIndex, postIndex, preorder, postorder)and return it.

Implementation
Complexity Analysis

Letnbe the size of the traversal arrays.

    Time complexity:O(n)

    We are makingnrecursive calls, one for each node in the tree. Each call of theconstructTreefunction involves only constant-time operations, like comparing values and incrementing pointers, and therefore the overall time complexity isO(n).

    Space complexity:O(n)

    Since we are not using any additional data structures, the auxiliary space complexity is determined by the recursion depth. In the worst case (when thepostorderarray contains the nodes in reverse order from thepreorderarray), we makenrecursive calls to create all the nodes before starting to backtrack. Therefore, the recursion depth can reachO(n), which also corresponds to the space complexity of the algorithm.
