Solution
Overview

We need to balance a binary search tree rooted at therootsuch that the difference between the depths of the two subtrees of every node never exceeds one. As a reminder, the depth of a given node in a tree is the number of edges from the root of the tree to that node.

    Note: Binary search trees (BSTs) are structured such that the value of each node is greater than all values in its left subtree and less than all values in its right subtree. Please refer to LeetCode's Explore Card on binary trees for a more detailed explanation:Binary Trees

We call such BSTs balanced BSTs. Balanced BSTs are efficient because they keep the tree height low, usually in logarithmic proportion to the number of nodes. This balance allows operations like insertion, deletion, and lookup to be done in logarithmic time on average. Keeping the tree balanced prevents it from becoming too deep, which would otherwise slow these operations down to linear time. This efficiency makes balanced BSTs ideal for tasks that need fast updates and quick searches.

There are two main approaches to balance a BST.

The first approach is to traverse and store all the BST nodes in a sorted array, then reconstruct the BST from scratch. Storing the values in sorted order ensures the new tree maintains the BST properties, where each node's left subtree contains only values less than the node's value, and the right subtree contains only values greater.

The second approach is to balance the BST in-place by restructuring it without additional storage. This involves performing rotations and rearrangements directly on the existing nodes to achieve balance while preserving BST properties.

This approach is more complex and is unlikely to be asked in an interview setting. However, it's worth understanding for deeper insights into tree rotations, balancing techniques, and the workings of self-balancing trees like AVL and Red-Black trees.
Approach 1: Inorder Traversal + Recursive Construction
Intuition

In the overview, we mentioned the need to traverse and store the nodes of the BST in increasing order. This can be achieved by iteratively visiting each node in the following order: first the left subtree, then the node itself, and finally the right subtree, known as an inorder traversal.

If you are not familiar with the three main traversal methods (inorder, preorder, and postorder), we encourage you to read about them here:

    Inorder Traversal
    Preorder Traversal
    Postorder Traversal

We can perform the inorder traversal either recursively or iteratively. In this editorial, we will use the recursive approach for its simplicity and brevity, though you are encouraged to try both methods.

With the nodes of the BST stored in an array in increasing order, we can now reconstruct the BST to be balanced.

The stored values in the array have a convenient property: for any given element that serves as the root, all elements to its left belong to the left subtree, and all elements to its right belong to the right subtree. To construct a balanced BST, we pick the middle element of the array as the root, ensuring the number of elements in the left and right subtrees differs by at most one. We then recursively apply the same process to the left and right subarrays to build the left and right subtrees. This approach ensures the balanced property of the BST.

Current
Algorithm

    Initialization:
        Create an empty listinorderto store the nodes' values after the inorder traversal.
    Perform inorder traversal:
        Traverse the BST and populate theinorderlist with the node values in sorted order.
    Reconstruct the balanced BST:
        Define a recursive functioncreateBalancedBSTthat takes theinorderlist,startindex, andendindex as parameters.
            Ifstartis greater thanend, returnnull(or equivalent).
            Calculate themidindex as the middle of the current range.
            Create a new tree node with the value at themidindex.
            Recursively build the left subtree using the left half of the current range.
            Recursively build the right subtree using the right half of the current range.
    Return the root of the newly constructed balanced BST.

Implementation
Complexity Analysis

Letnbe the number of nodes in the BST.

    Time Complexity:O(n)

    TheinorderTraversalfunction visits each node exactly once, resulting in a time complexity ofO(n).

    Constructing the balanced BST with thecreateBalancedBSTfunction also involves visiting each node exactly once, resulting in a time complexity ofO(n).

    Therefore, the overall time complexity isO(n).

    Space Complexity:O(n)

    TheinorderTraversalfunction uses an additional array to store the inorder traversal, which requiresO(n)space.

    The recursive calls in theinorderTraversalandcreateBalancedBSTfunctions contribute to the space complexity. In the worst case, the recursion stack can grow toO(n)for a skewed tree.

    Therefore, the overall space complexity isO(n).

Approach 2: Day-Stout-Warren Algorithm / In-Place Balancing
Intuition

    Note:This approach is very advanced and would not be expected in an interview. We have included it for completeness.

The Day-Stout-Warren (DSW) algorithm provides an in-place method for balancing Binary Search Trees (BSTs). To understand DSW, we first need to grasp the concept of rotations, which are fundamental operations for restructuring the tree to reduce its height and improve balance.

Rotations come in two forms:

    Right Rotation: This operation elevates the left child of a node to take its place, while the original node becomes the right child of its former left child.
    Left Rotation: Conversely, this operation elevates the right child of a node to take its place, with the original node becoming the left child of its former right child.

It's important to note that right and left rotations are inverse operations, each undoing the effect of the other.

rotate1

With this foundation, we can now explore how DSW leverages these rotations. The algorithm employs a three-phase approach to balance a BST:

    Create the Backbone (vine)

In this initial phase, DSW transforms the BST into a right-skewed tree, resembling a vine or linked list. This is achieved through a series of right rotations. The process involves traversing the tree and performing a right rotation whenever a node with a left child is encountered, continuing until the entire tree is right-skewed.

The slideshow is shown below:

Current

    Count the nodes

Once the backbone is created, the next step is to determine the total number of nodes in the vine. This is done by traversing the right-skewed structure and counting each node. Let's denote this count asn. This count becomes crucial for the final balancing phase.

    Balance the vine

The final phase aims to convert the right-skewed vine into a balanced BST. This is accomplished through a series of left rotations. The process begins by calculatingm, which is the largest power of 2 less thann + 1, minus 1. This calculation is significant as it identifies the largest complete subtree that can be fully balanced.

The balancing then proceeds in two steps:

a) Performn - mleft rotations to partially balance the tree. This ensures that the remaining nodes will form a complete binary tree after the first set of rotations.

b) Enter a loop wheremis halved repeatedly. For each iteration, perform left rotations to balance the next level of the tree. This process continues until the vine is fully transformed into a balanced BST.

Current

    Note:While this approach is space-efficient, it modifies the tree structure during traversal, which might not be suitable in all scenarios, especially if the tree is being accessed concurrently by other processes. The constant modification of tree links may have a slight impact on performance compared to straightforward recursive approaches, especially for smaller trees.

Algorithm

    Initialization:
        If the root isnull, returnnull.
        Create a temporary dummy nodevineHead.
        Set the right child ofvineHeadas the root of the BST.
        Initialize a pointercurrenttovineHead.
    Create the Backbone (Vine):
        Whilecurrenthas a right child:
            Ifcurrent's right child has a left child:
                Perform a right rotation oncurrentand its right child.
            Otherwise:
                Movecurrentto its right child.
    Count the Nodes:
        InitializenodeCountto 0.
        Setcurrentas the right child ofvineHead.
        Whilecurrentis notnull:
            IncrementnodeCount.
            Movecurrentto its right child.
    Create a Balanced BST:
        Calculatemas the largest power of 2 less thannodeCount + 1minus 1.
        PerformnodeCount - mleft rotations on the vine to partially balance it.
        Whilemis greater than 1:
            Halvem.
            Performmleft rotations on the vine to further balance it.
    Return the Balanced BST:
        SetbalancedRootto the right child ofvineHead.
        Delete the temporary dummy nodevineHead.
        ReturnbalancedRoot.

    Right Rotation:
        Given a parent node and its right child:
            Settmpto the left child of the right child.
            Set the left child of the right child to the right child oftmp.
            Set the right child oftmpto the right child of the parent node.
            Set the right child of the parent node totmp.
    Left Rotation:
        Given a parent node and its right child:
            Settmpto the right child of the right child.
            Set the right child of the right child to the left child oftmp.
            Set the left child oftmpto the right child of the parent node.
            Set the right child of the parent node totmp.
    Make Rotations:
        GivenvineHeadandcount:
            SetcurrenttovineHead.
            Forifrom 0 tocount - 1:
                Settmpto the right child ofcurrent.
                Perform a left rotation oncurrentandtmp.
                Movecurrentto its right child.

Implementation
Complexity Analysis

Letnbe the number of nodes in the BST atroot.

    Time Complexity:O(n)

    The loop that creates the vine visits each node exactly once, and each right rotation isO(1), resulting inO(n)time.

    Counting nodes in the vine involves a single traversal of the vine, which isO(n).

    ThemakeRotationsfunction performs a series of left rotations. Each rotation isO(1), and the total number of rotations across all iterations isO(n). Although the number of rotations is bounded by a logarithmic factor due to iteratively halvingm, the overall complexity remainsO(n)due to the linear traversal and rotation steps.

    Therefore, the overall time complexity isO(n).

    Space Complexity:O(n)

    The algorithm primarily uses a temporary pointer structure and the original nodes, contributing toO(1)additional space. The vine structure uses the existing nodes in-place, without requiring extra memory.

    However, the depth of the recursion stack in the worst case can reachO(n)if the tree is skewed.

    Therefore, the overall space complexity isO(n).
