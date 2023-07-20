# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def is_present(node, r,s):
            if node is None:
                return node
            if node==r or node==s:
                return node
            left = is_present(node.left,r,s) 
            right = is_present(node.right,r,s)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
        return is_present(root,p,q)


