# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(root):
            if root is None:
                return root
            else:
                if root.right is None and root.left is not None:
                    root.right = flat(root.left)
                    root.left = None
                elif root.right is not None and root.left is None:
                    root.right = flat(root.right)
                elif root.right is not None and root.left is not None:
                    temp = root.right
                    root.right = flat(root.left)
                    ptr = root.right
                    while ptr.right is not None:
                        ptr = ptr.right
                    ptr.right = flat(temp)
                    root.left = None
                else:
                    return root
            return root

        root = flat(root)
