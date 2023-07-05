# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None or root.right is None:
            l = 10**6
            r = 10**6
            if root.left is None:
                l = self.minDepth(root.right)
            if root.right is None:
                r = self.minDepth(root.left)
            return 1 + min(l,r)
        else:
            return 1 + min(self.minDepth(root.right),self.minDepth(root.left))