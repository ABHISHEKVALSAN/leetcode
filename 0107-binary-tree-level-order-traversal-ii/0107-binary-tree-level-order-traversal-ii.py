# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def traverse(root):
            queue = deque()
            queue.append((0,root))
            max_depth = 0
            while queue:
                depth, node = queue.popleft()
                max_depth = max(depth, max_depth)
                result.append((depth,node.val))
                if node.left is not None:
                    queue.append((depth+1,node.left))
                if node.right is not None:
                    queue.append((depth+1,node.right))
            return max_depth
        if root is None:
            return root
        max_depth = traverse(root)
        new_result = [[] for i in range(max_depth+1)]
        for depth, val in result:
            new_result[depth].append(val)
        return new_result[::-1]
