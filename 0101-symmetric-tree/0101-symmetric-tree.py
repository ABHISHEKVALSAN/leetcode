# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p is None or q is None:
                return p==q
            else:
                return  p.val==q.val and \
                        isSameTree(p.left,q.right) and \
                        isSameTree(p.right, q.left)
        return True if root is None else isSameTree(root.right,root.left)
        