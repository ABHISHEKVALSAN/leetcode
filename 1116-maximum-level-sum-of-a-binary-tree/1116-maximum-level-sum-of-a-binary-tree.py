# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def bfs(self, Tree):
        lvl = 1
        queue = deque([[Tree,1]])
        bfs = []
        while queue:
            current_node, lvl = queue.popleft()
            bfs.append([current_node.val,lvl])
            if current_node.left is not None:
                queue.append([current_node.left,lvl+1])
            if current_node.right is not None:
                queue.append([current_node.right, lvl+1])
        #print(bfs)
        return bfs

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        bfs_list = self.bfs(root)

        max_lvl = 1
        max_sum = 0

        current_lvl = 1
        current_sum = 0

        i = 0

        max_lvl = 1
        max_sum = -10**5 -1
        n = len(bfs_list)
        while i < n:
            current_lvl = bfs_list[i][1]
            current_sum = bfs_list[i][0]
            i+=1
            while i < n and bfs_list[i][1]==current_lvl:
                current_sum+=bfs_list[i][0]
                i+=1
            if current_sum > max_sum:
                max_sum = current_sum
                max_lvl = current_lvl
            #print(current_sum, current_lvl, max_sum, max_lvl)
        return max_lvl


