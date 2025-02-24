# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = root
        self.values = set()
        self.dfs(self.tree, 0)


    def dfs(self, root, x):
        if root is None:
            return

        root.val = x
        self.values.add(x)
        self.dfs(root.left, 2 * x + 1)
        self.dfs(root.right, 2 * x + 2)

    def find(self, target: int) -> bool:
        return target in self.values
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)