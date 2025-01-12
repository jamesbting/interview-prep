# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = []
        q = Queue()
        q.put(root)
        while not q.empty():
            curr = q.get()

            if curr is None:
                tree.append("null")
            else:
                tree.append(str(curr.val))
                q.put(curr.left)
                q.put(curr.right)

        return "|".join(tree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        node_list = data.split("|")

        if len(node_list) <= 1:
            return None

        root = TreeNode(int(node_list[0]))
        q = [root]
        node_list = node_list[1:]        
        while len(q) > 0:
            curr = q.pop(0)
            if len(node_list) > 0:
                next_left = node_list.pop(0)
                if  next_left != "null":
                    curr.left = TreeNode(int(next_left))
                    q.append(curr.left)
                
            if len(node_list) > 0:
                next_right = node_list.pop(0)
                if next_right != "null":
                    curr.right = TreeNode(int(next_right))
                    q.append(curr.right)
                
        return root



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))