# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root, val, left):
            if root==None:
                return True
            if left==True:
                if root.val >= val:
                    return False
                return solve(root.left, val, True) and solve(root.right, val, True)
            else:
                if root.val <= val:
                    return False
                return solve(root.left, val, False) and solve(root.right, val, False)
        if root==None:
            return True
        return solve(root.left, root.val, True) and solve(root.right, root.val, False) and self.isValidBST(root.left) and self.isValidBST(root.right)

