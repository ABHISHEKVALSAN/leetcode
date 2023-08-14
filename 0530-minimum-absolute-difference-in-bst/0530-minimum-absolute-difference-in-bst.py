# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def get_max(node):
            val = node.val
            while node:
                val = node.val
                node = node.right
            return val
        def get_min(node):
            val = node.val
            while node:
                val = node.val
                node = node.left
            return val
        def solve(root):
            s1=s2=s3=s4=10**9
            if root.right is not None:
                s1 = abs(root.val - get_min(root.right))
                s2 = solve(root.right)
            if root.left is not None:
                s3 = abs(root.val - get_max(root.left))
                s4 = solve(root.left)
            return min(s1,s2,s3,s4)
        return solve(root)