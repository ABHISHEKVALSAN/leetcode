# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return []
        def solve(root):
            stack = [[root,0]]
            max_depth = -1
            while stack:
                curr, depth = stack.pop()
                if depth>max_depth:
                    max_depth = depth
                    ans.append(curr.val)
                if curr.left is not None:
                    stack.append([curr.left,depth+1])
                if curr.right is not None:
                    stack.append([curr.right,depth+1])
        solve(root)
        return ans