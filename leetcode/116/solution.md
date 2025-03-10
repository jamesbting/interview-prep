Solution
Approach 1: Level Order Traversal

Intuition

There are two basic kinds of traversals on a tree or a graph. One is where we explore the tree in a depth first manner i.e. one branch at a time. The other one is where we traverse the tree breadth-wise i.e. we explore one level of the tree before moving on to the next one. For trees, we have further classifications of the depth first traversal approach called preorder, inorder, and the postorder traversals. Breadth first approach to exploring a tree is based on the concept of the level of a node. The level of a node is its depth or distance from the root node. We process all the nodes on one level before moving on to the next one.

Now that we have the basics out of the way, it's pretty evident that the problem statement strongly hints at a breadth first kind of a solution. We need to link all the nodes together which lie on the same level and the level order or the breadth first traversal gives us access to all such nodes.

Algorithm

    Initialize a queue, Q which we will be making use of during our traversal. There are multiple ways to implement the level order traversal especially when it comes to identifying the level of a particular node.

        We can add a pair of (node,level) to the queue and whenever we add the children of a node, we add (node.left,parent_level+1) and (node.right,parent_level+1). This approach wouldn't be very efficient for our algorithm since we need all the nodes on the same level and we would need another data structure just for that.

        A more memory efficient way of segregating the same level nodes is to use some demarcation between the levels. Usually, we insert a NULL entry in the queue which marks the end of the previous level and the start of the next level. This is a great approach but again, it would still consume some memory proportional to the number of levels in the tree.

        The approach we will be using here would have a nested loop structure to get around the requirement of a NULL pointer. Essentially, at each step, we record the size of the queue and that always corresponds to all the nodes on a particular level. Once we have this size, we only process these many elements and no more. By the time we are done processing size number of elements, the queue would contain all the nodes on the next level. Here's a pseudocode for the same:

         while (!Q.empty())
         {
             size = Q.size()
             for i in range 0..size
             {
                 node = Q.pop()
                 Q.push(node.left)
                 Q.push(node.right)
             }
         }
         

    We start off by adding the root of the tree in the queue. Since there is just one node on the level 0, we don't need to establish any connections and can move onto the while loop.

    The first while loop from the pseudocode above essentially iterates over each level one by one and the inner for loop iterates over all the nodes on the particular level. Since we have access to all the nodes on the same level, we can establish the next pointers easily.

    When we pop a node inside the for loop from the pseudocode above, we add its children at the back of the queue. Also, the element at the head of the queue is the next element in order, on the current level. So, we can easily establish the new pointers.

Complexity Analysis

    Time Complexity: O(N) since we process each node exactly once. Note that processing a node in this context means popping the node from the queue and then establishing the next pointers.
    Space Complexity: O(N). This is a perfect binary tree which means the last level contains N/2 nodes. The space complexity for breadth first traversal is the space occupied by the queue which is dependent upon the maximum number of nodes in particular level. So, in this case, the space complexity would be O(N).


Approach 2: Using previously established next pointers

Intuition

Let's look at the two types of next pointer connections we need to establish for a given tree.

    This first case is the one where we establish the next pointers between the two children of a given node. This is the easier of the two cases since both the children are accessible via the same node. We can simply do the following to establish this connection.

     node.left.next = node.right

    This next case is not too straightforward to handle. In addition to establishing the next pointers between the nodes having a common parent, we also need to set-up the correct pointers between nodes which have a different parent.

If we simply had the parent pointers available with each node, this problem would have been trivial to solve. However, we don't have any such pointers available. The basic idea for this approach is based on the fact that:

    We only move on to the level N+1 when we are done establishing the next pointers for the level N. Since we have access to all the nodes on a particular level via the next pointers, we can use these next pointers to establish the connections for the next level or the level containing their children.

Algorithm

    We start at the root node. Since there are no more nodes to process on the first level or level 0, we can establish the next pointers on the next level i.e. level 1. An important thing to remember in this algorithm is that we establish the next pointers for a level N while we are still on level N−1 and once we are done establishing these new connections, we move on to N and do the same thing for N+1.

    As we just said, when we go over the nodes of a particular level, their next pointers are already established. This is what helps get rid of the queue data structure from the previous approach and helps save space. To start on a particular level, we just need the leftmost node. From there on out, its just a linked list traversal.

    Based on these ideas, our algorithm will have the following pseudocode:

     leftmost = root
     while (leftmost.left != null)
     {
         head = leftmost
         while (head != null)
         {
             1) Establish Connection 1
             2) Establish Connection 2 using next pointers
             head = head.next
         }
         leftmost = leftmost.left
     }

    The Connection 1 and Connection 2 mentioned above correspond to the two kinds of connections we looked at earlier on in the intuition section of this approach.

        The first one is fairly simple to establish given that it's between the two nodes having a common parent. So, we could simply do something like this to link the two children:

         node.left.next = node.right
         

        For the second type of connection, we have to make use of the next pointers on the current level. Remember that this second type of connection is between nodes that have different parents. More specifically, it's the link between the right child of a node and the left child of the next node. Since we already have the next pointers set up on the current level, we use this to set up the correct pointers on the next level.

        node.right.next = node.next.left

    Once we are done with the current level, we move on to the next one. One last thing that's left here is to update the leftmost node. We need that node to start traversal on a particular level. Think of it as the head of the linked list. Since this is a perfect binary tree, the leftmost node will always be the left child of the current leftmost node. The only nodes which don't have any children are the ones on the final level and these would be the leaves of the tree.

Complexity Analysis

    Time Complexity: O(N) since we process each node exactly once.
    Space Complexity: O(1) since we don't make use of any additional data structure for traversing nodes on a particular level like the previous approach does. 