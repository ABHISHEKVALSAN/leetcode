from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(v):
            if v in safe_nodes:
                return False
            visited.add(v)
            stack.add(v)
            for neighbor in graph[v]:
                if neighbor in stack:
                    return True
                if neighbor not in visited and dfs(neighbor):
                    return True
            stack.remove(v)
            return False
        g = {}
        visited = set()
        stack = set()
        for ind, nodes in enumerate(graph):
            if ind not in g:
                g[ind] = []
            for node in nodes:
                g[ind].append(node)
        safe_nodes = []
        for ind, nodes in enumerate(graph):
            if len(nodes)==0:
                safe_nodes.append(ind)
        print('sn', safe_nodes)
        ans = []
        for node in g.keys():
            if not dfs(node):
                ans.append(node)
            #print('ans',ans)
        return ans



