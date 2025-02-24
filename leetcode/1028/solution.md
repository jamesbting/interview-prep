Overview
We are given a string representation of a preorder traversal of a binary tree, where each node is represented asDdashes followed by its value. The number of dashesDindicates the depth of the node in the tree, with the root having depth0. Each node may have one or two children, and if a node has only one child, it is always the left child. Our task is to reconstruct the original binary tree from this traversal string.

Since preorder traversal follows theroot → left → rightorder, we process the nodes in sequence and assign them to their correct positions.

For example, giventraversal = "1-2--3--4-5--6--7", we can break it down as follows:

1  (Root)
|- 2  (Depth 1, Left child of 1)
|  |- 3  (Depth 2, Left child of 2)
|  |- 4  (Depth 2, Right child of 2)
|- 5  (Depth 1, Right child of 1)
   |- 6  (Depth 2, Left child of 5)
   |- 7  (Depth 2, Right child of 5)
This means the tree structure is:

       1
      / \
     2   5
    / \  / \
   3   4 6  7
The output should be:[1, 2, 5, 3, 4, 6, 7].

Before diving into specific approaches, let’s first build a high-level strategy that applies to all the approaches.

Depth determines hierarchy
Each node’s position in the tree is determined by the number of dashes (-) before its value:

A node with depthDis the child of the last node with depthD - 1.
If a node has a sibling, it appears immediately after its left sibling in the traversal.
If a node does not have a sibling, it is the only child of its parent.
This means that the structure of the tree is fully determined by depth information, without requiring additional information like explicit left/right indicators. Because nodes appear before their children in preorder, we can sequentially assign them to their parents without needing to look ahead or backtrack significantly.

Maintaining a Structure to Track Parent-Child Relationships
To efficiently determine the correct parent for each node, we need a mechanism to track nodes at different depths. There are two main ways to do this:

Using Recursion: We can recursively parse the string and build the tree.
Using Stack: We maintain a stack where each node is pushed when encountered. When we process a new node, we find its correct parent by checking the stack for the most recent node withdepth - 1.
Regardless of the approach, the core idea is the same: When we encounter a new node, we determine its depth. We find the last node atdepth - 1and attach the new node as its child. Then we ensure that the first child assigned to a parent is the left child, and the second (if present) is the right child.

Approach 1: Brute Force (Recursive with String Manipulation)
Intuition
The simplest way to reconstruct a tree from a string is to process the input step by step as the input is in the format of preorder traversal. We know that each number in the string represents a node in the tree, and the number of dashes before it tells us how deep it should be.

To build the tree, first, we count the number of dashes (-). The more dashes we see, the deeper the node is in the tree. After counting the dashes, we extract the number that follows. This number becomes the value of a new node.

Once we have a node, we need to figure out where to place it in the tree. Since the nodes appear in depth-first (preorder) order in the string, we know that every new node belongs as a child of the most recently encountered node that has space for a child. If a node is at a greater depth than the previous one, it must be its left child. If it's at the same depth as the last node, it means we have moved to a new subtree, and it should be attached as a right child instead.

To implement this, we use recursion. A helper function takes the string and the current index, processes the node at that position, and then calls itself to construct the left and right children. This recursion follows the same logic as a depth-first traversal of a tree. If the function encounters a node at the wrong depth, it stops and returns, ensuring that nodes are placed correctly.

For a more comprehensive understanding of recursion, check out theRecursion Explore Card 🔗.

Algorithm
Start withindex = 0and call the recursivehelperfunction withdepth = 0.

Inhelperfunction:

Ifindexexceeds the length oftraversal, returnnullptr.

Count the number of dashes (dashCount) atindex:

Iterate while the character atindex + dashCountis'-'.
IncreasedashCountaccordingly.
IfdashCountdoes not matchdepth, returnnullptr(ensures correct tree structure).

Moveindexpast the dashes.

Extract the numeric value for the node:

Initializevalue = 0.
Whileindexpoints to a digit, updatevalueusingvalue * 10 + (digit).
Incrementindexfor each digit processed.
Create a newTreeNodewith the extracted value.

Recursively construct left and right children:

Callhelperwithdepth + 1for the left subtree.
Callhelperwithdepth + 1for the right subtree.
Return the constructedTreeNode.

Implementation

Complexity Analysis
Letnbe the length of the input stringtraversal.

Time complexity:O(n)

We traverse the stringtraversalexactly once while parsing node values and dashes. Each character in the string is processed a constant number of times—either when counting dashes or extracting numeric values.

The recursive functionhelperis called once for each node in the tree, and since there are at mostO(n)nodes (each digit contributes to a node value), the number of recursive calls is also bounded byO(n).

As a result, the overall time complexity isO(n).

Space complexity:O(n)

The recursion depth is determined by the depth of the binary tree, which in the worst case (a skewed tree) can beO(n). This leads to anO(n)recursive call stack space.

Additionally, we allocateO(n)newTreeNodeobjects, contributing to an extraO(n)memory usage.

Thus, the overall space complexity isO(n).

Approach 2: Iterative Approach with Stack
Intuition
Recursion is useful, but it can be slow because it involves extra function calls and memory overhead. A more efficient way to process the string is to use a stack to keep track of nodes as we build the tree.

Think of the stack as a way to remember where we are in the tree. Each time we find a new node, we check how deep it should be by counting dashes. If the stack already has more nodes than this depth, it means we have finished processing a subtree, so we remove nodes from the stack until we reach the correct depth. The node left at the top of the stack is the parent of the new node.

Once we identify the parent, we decide whether to attach the new node as its left or right child. If the left child doesn’t exist, we set it as the left child. Otherwise, it must be the right child. Finally, we push the new node onto the stack because it might have its own children in later steps.

For a more comprehensive understanding of stacks, check out theStack Explore Card 🔗.

Algorithm
Initialize a stack to store nodes along with their depth.

Setindexto 0 for traversing the input string.

Initializerootasnullptrto store the root node.

Iterate throughtraversaluntil all characters are processed:

Count the number of dashes to determine the depth of the current node.
Extract the node's value by parsing consecutive digits.
Create a newTreeNodewith the extracted value.

Ifdepthis 0, assign this node as the root.

Otherwise:

Pop nodes from the stack until a parent node of the current depth is found.
Attach the new node as the left child if the parent's left isnullptr, otherwise as the right child.
Push the current node and its depth onto the stack.

Return the root node after constructing the tree.

Implementation

Complexity Analysis
Letnbe the length of the input stringtraversal.

Time complexity:O(n)

We traverse the stringtraversalexactly once while parsing the number of dashes and extracting numeric values. Each character is processed a constant number of times.

The stack operations (push and pop) are performed at most once per node. Since the total number of nodes is at mostO(n), the stack operations contributeO(n)in total.

Thus, the overall time complexity isO(n).

Space complexity:O(n)

The maximum depth of the tree determines the maximum size of the stack. In the worst case (a skewed tree), the depth can beO(n), leading to anO(n)stack size.

Additionally, we allocateO(n) TreeNodeobjects, contributing to an extraO(n)memory usage.

Thus, the overall space complexity isO(n).

Approach 3: Optimized Iterative Approach with Stack (Single Pass)
Intuition
The previous iterative approach works well, but it still requires us to track the depth explicitly. We can make it even more efficient by simplifying the depth tracking. Instead of storing depths separately, we use the size of the stack itself to determine the depth.

Since the stack always holds the path from the root to the current node, its length at any point represents how deep we are in the tree. When we encounter a new node, we count the dashes to determine its depth. If the stack is longer than the depth, it means we need to move up in the tree, so we remove nodes from the stack until it matches the correct depth.

After adjusting the stack, the node at the top is the parent of the new node. As before, we attach the new node as a left child if there’s space, otherwise as a right child. This method eliminates the need to explicitly store depth values, keeping everything in a single structure (the stack).

Algorithm
Initialize astackto keep track of nodes at different depths.

Initializeindexto 0 for traversing thetraversalstring.

Iterate whileindexis within the bounds oftraversal:

Count the number of dashes (-) to determine thedepthof the current node.
Extract the numerical value of the node by iterating through the digits.
Create a newTreeNodewith the extracted value.
Adjust thestackto ensure it aligns with the correct depth by popping elements if necessary.
Attach the newly created node to its parent:
If the top node of the stack has no left child, assign the new node as the left child.
Otherwise, assign it as the right child.
Push the new node onto the stack.
Ensure the root node is correctly identified by popping extra elements from the stack until only one remains.

Return the remaining node in the stack as the root of the reconstructed tree.

Implementation

Complexity Analysis
Letnbe the length of the input stringtraversal.

Time complexity:O(n)

We traverse the stringtraversalexactly once while counting dashes and extracting node values. Each character is processed a constant number of times, contributingO(n).

The stack operations (push and pop) are performed at most once per node. Since the total number of nodes is at mostO(n), the stack operations contributeO(n)in total.

Thus, the overall time complexity isO(n).

Space complexity:O(n)

The maximum depth of the tree determines the maximum size of the stack. In the worst case (a skewed tree), the depth can beO(n), leading to anO(n)stack size.

Additionally, we allocateO(n) TreeNodeobjects, contributing to an extraO(n)memory usage.

Thus, the overall space complexity isO(n).

Approach 4: Optimized Iterative Approach with Stack (No String Manipulation)
Intuition
We can optimize the previous approach by completely avoiding unnecessary string manipulations. The key improvement here is that instead of slicing the string or creating substrings, we process the input in a single pass, extracting numbers and dashes.

Just like in previous approaches, we iterate through the string while keeping track of depth using dashes. The difference is that we never store or manipulate substrings—we just increment the index while reading the characters directly. This minimizes unnecessary operations and speeds up execution.

After extracting a node’s value, we adjust the stack depth to ensure that the new node is inserted at the correct position in the tree. By popping elements from the stack when necessary, we ensure that the top node in the stack is the parent. We then attach the new node to the left or right child accordingly.

The algorithm is visualized below:

approach__4

Algorithm
Initialize an emptystackto store nodes and setindexto 0.

Determine the lengthnof the traversal string.

Iterate whileindexis less thann:

Count the number of dashes to determine the depth of the node.
Extract the node value by converting consecutive digits to an integer.
Create a newTreeNodewith the extracted value.
Adjust the stack to the correct depth by popping excess nodes.
Attach the new node to its parent:
If the top node in the stack has no left child, assign the new node as the left child.
Otherwise, assign it as the right child.
Push the new node onto the stack.
After the loop, remove extra nodes from the stack until only the root remains.

Return the root node, which is the last remaining node in the stack.

Implementation

Complexity Analysis
Letnbe the length of the input stringtraversal.

Time complexity:O(n)

We traverse the stringtraversalexactly once to count dashes and extract numeric values. Each character is processed a constant number of times, leading to anO(n)traversal.

Stack operations (push and pop) are performed at most once per node. Since there are at mostO(n)nodes in the tree, these stack operations contribute an additionalO(n).

Thus, the overall time complexity isO(n).

Space complexity:O(n)

The maximum size of the stack is determined by the depth of the tree. In the worst case (a skewed tree), the depth can beO(n), leading to anO(n)stack size.

Additionally, we allocateO(n) TreeNodeobjects, contributing to an extraO(n)memory usage.

Thus, the overall space complexity isO(n).