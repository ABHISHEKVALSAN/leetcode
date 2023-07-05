# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root):
            if root is None:
                return 0
            else:
                return 1 + max(getDepth(root.left),getDepth(root.right))
        if root is None:
            return True
        ld = getDepth(root.left)
        rd = getDepth(root.right)

        return abs(ld -rd)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        