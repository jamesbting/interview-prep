Solution
Approach 1: Construct binary tree from preorder and inorder traversal
Intuition

This approach is not the optimal one because of O(NlogN) time complexity, but very straightforward.

Let's use here two facts:

Binary tree could be constructed from preorder and inorder traversal.

Inorder traversal of BST is an array sorted in the ascending order.

Algorithm

Construct inorder traversal by sorting the preorder array.

Construct binary tree from preorder and inorder traversal:
the idea is to peek at the elements one by one from the preorder array and try to put them as a left or as a right child if it's possible. If it's impossible - just put null as a child and proceed further. The possibility to use an element as a child is checked by an inorder array: if it contains no elements for this subtree, then the element couldn't be used here, and one should use null as a child instead.

Implementation

bla


Complexity Analysis

Time complexity : O(NlogN). O(NlogN) to sort preorder array
and O(N) to construct the binary tree.
Space complexity : O(N) the inorder traversal and the tree.


Approach 2: Recursion
Intuition

It's quite obvious that the best possible time complexity for this problem
is O(N) and hence approach 1 is not the best one.

Basically, the inorder traversal above was used only to check if the element
could be placed in this subtree.
Since one deals with a BST here, this could be verified with the help of lower and
upper limits for each element as for the validate BST problem.
This way there is no need for inorder traversal and the time
complexity is O(N).

Algorithm

Initiate the lower and upper limits as negative and positive infinity because
one could always place the root.

Start from the first element in the preorder array idx = 0.

Return helper(lower, upper):

If the preorder array is used up idx = n then the tree is constructed, return null.

If the current value val = preorder[idx] is smaller than the lower limit, or larger than the upper limit, return null.

If the current value is in the limits, place it here root = TreeNode(val)
and proceed to construct recursively left and right subtrees:
root.left = helper(lower, val) and root.right = helper(val, upper).

Return root.

Implementation

bla


Complexity Analysis

Time complexity : O(N) since we visit each node exactly once.
Space complexity : O(N) to keep the entire tree.

Approach 3: Iteration
Algorithm

The recursion above could be converted into the iteration, with the help of stack.

Pick the first preorder element as a root root = new TreeNode(preorder[0]) and push it into stack.

Use for loop to iterate along the elements of a preorder array :

Pick the last element of the stack as a parent node, and the current element of preorder as a child node.

Adjust the parent node: pop out of stack all elements with a value smaller than the child value. Change the parent node at each pop node = stack.pop().

If node.val < child.val - put the child as a right child of the node: node.right = child.

Else - as a left child : node.left = child.

Push the child node into the stack.

Return root.

Implementation

Current


Complexity Analysis

Time complexity : O(N) since we visit each node exactly once.

Space complexity : O(N) to keep the stack and the tree.