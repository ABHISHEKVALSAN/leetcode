# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [root]
        count=0
        while stack:
            curr = stack.pop()
            count+=1
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
        return count