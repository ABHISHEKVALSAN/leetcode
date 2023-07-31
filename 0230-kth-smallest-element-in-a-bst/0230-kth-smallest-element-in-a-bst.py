# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def traverse(root):
            if root==None:
                return
            traverse(root.left)
            result.append(root.val)
            traverse(root.right)
        traverse(root)
        print(result)
        return result[k-1]