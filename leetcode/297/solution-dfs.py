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
        stack = []

        def dfs(curr):
            if curr is None:
                stack.append("N")
                return
            stack.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return "|".join(stack)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = [int(s) if s != "N" else None for s in data.split("|")]
        global index
        index = -1
        def dfs(l):
            global index
            index += 1
            if l[index] == None:
                return None

            root = TreeNode(l[index])
            root.left = dfs(l)
            root.right = dfs(l)
            return root
            
        root = dfs(nodes)
        return root



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))