"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        result = []
        def bfs(node):
            queue = deque([[node,0]])
            curr_nodes = []
            curr_depth = 0
            while queue:
                curr, depth = queue.popleft()
                if curr.left is not None:
                    queue.append([curr.left,depth+1])
                if curr.right is not None:
                    queue.append([curr.right,depth+1])
                if depth==curr_depth:
                    curr_nodes.append(curr)
                else:
                    result.append(curr_nodes)
                    curr_nodes = [curr]
                    curr_depth = depth
            result.append(curr_nodes)
        if root is not None:
            bfs(root)
        for node_list in result:
            i = 0
            while i<len(node_list)-1:
                node_list[i].next = node_list[i+1]
                i+=1
        return root

