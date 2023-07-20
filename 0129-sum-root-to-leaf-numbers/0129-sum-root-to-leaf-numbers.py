# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [[0,root]]
        ans = 0
        while stack:
            prev, curr = stack.pop()
            if curr.left is None and curr.right is None:
                ans += prev*10 +curr.val
            else:
                if curr.left is not None:
                    stack.append([prev*10+curr.val,curr.left])
                if curr.right is not None:
                    stack.append([prev*10+curr.val,curr.right])
        return ans