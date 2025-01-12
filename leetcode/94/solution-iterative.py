class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        ans = []
        while curr is not None or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
            
        return ans