# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def solve(root):
            if root is not None:
                if root.right is None and root.left is None:
                    yield f"{root.val}"
                else:
                    for ans in solve(root.left):
                        yield f"{root.val}->{ans}"
                    for ans in solve(root.right):
                        yield f"{root.val}->{ans}"
        result=[]
        for ans in solve(root):
            result.append(ans)
        return result
                