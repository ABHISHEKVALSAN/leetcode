from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        i = 0
        n = len(values)
        graph = {}
        while i < n:
            a,b = equations[i]
            ans = values[i]
            graph[a] = graph.get(a,set()).union(set([(b,ans)]))
            if ans:
                graph[b] = graph.get(b,set()).union(set([(a,1/ans)]))
            i+=1
        def bfs(start,target):
            queue = deque()
            vis = set()
            queue.append((start,1.0))
            vis.add(start)
            while queue:
                curr, mul = queue.popleft()
                for vertex, weight in graph[curr]:
                    if vertex==target:
                        print(weight*mul,end=',')
                        return weight * mul
                    if vertex not in vis:
                        vis.add(vertex)
                        queue.append((vertex,mul*weight))
            return -1.0
        result = []
        for a,b in queries:
            if a not in graph or b not in graph:
                result.append(-1)
            elif a==b:
                result.append(1)
            else:
                result.append(bfs(a,b))
        return result
            
