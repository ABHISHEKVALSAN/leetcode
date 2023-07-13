# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def traverse(root):
            if root is None:
                return []
            queue = deque()
            queue.append([root,1])
            while queue:
                curr, depth = queue.popleft()
                ans.append([curr.val,depth])
                if curr.left is not None:
                    queue.append([curr.left,depth+1])
                if curr.right is not None:
                    queue.append([curr.right,depth+1])
        traverse(root)
        if len(ans)==0:
            return []
        result = [[ans[0][0]]]
        curr_depth = ans[0][1]
        for node_val, depth in ans[1:]:
            if depth==curr_depth:
                result[-1].append(node_val)
            else:
                curr_depth = depth
                result.append([node_val])

        return result

        