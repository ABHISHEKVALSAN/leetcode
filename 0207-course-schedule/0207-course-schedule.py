class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {}
        for v1,v2 in prerequisites:
            if v2 in g:
                g[v2].add(v1)
            else:
                g[v2] = set([v1])
            if v1 not in g:
                g[v1] = set([])
        print(g)
        def has_cycle():
            visited = set()
            stack = set()
            def dfs(v):
                stack.add(v)
                visited.add(v)
                for neighbor in g[v]:
                    if neighbor in stack:
                        return True
                    if neighbor not in visited and dfs(neighbor):
                        return True
                stack.remove(v)
                return False
            for v in g:
                if dfs(v):
                    return True
            return False
        return has_cycle()==False