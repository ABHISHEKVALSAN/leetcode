# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def __init__(self):
        self.graph = {}
        self.ans = []
    def traverse(self,root):
        if root is not None:
            if root.left is not None:
                if root.val in self.graph:
                    self.graph[root.val].add(root.left.val)
                else:
                    self.graph[root.val] = {root.left.val}
                if root.left.val in self.graph:
                    self.graph[root.left.val].add(root.val)
                else:
                    self.graph[root.left.val] = {root.val}
                self.traverse(root.left)
            if root.right is not None:
                if root.val in self.graph:
                    self.graph[root.val].add(root.right.val)
                else:
                    self.graph[root.val] = {root.right.val}
                if root.right.val in self.graph:
                    self.graph[root.right.val].add(root.val)
                else:
                    self.graph[root.right.val] = {root.val}
                self.traverse(root.right)

    def bfs(self,v,k):
        queue = deque()
        queue.append([v,0])
        visited ={ch:False for ch in self.graph}
        while queue:
            curr_v, depth = queue.popleft()
            visited[curr_v] = True
            if depth==k:
                self.ans.append(curr_v)
            else:
                if curr_v in self.graph:
                    for new_v in self.graph[curr_v]:
                        if not visited[new_v]:
                            queue.append([new_v, depth+1])
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.traverse(root)
        self.bfs(target.val,k)
        return self.ans
