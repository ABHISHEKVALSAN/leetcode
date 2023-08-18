from itertools import combinations
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads)==0:
            return 0
        if len(roads)==1:
            return 1
        g = {i:set([]) for i in range(n)}
        for i,j in roads:
            g[i].add(j)
            g[j].add(i)
        print(g)
        ans = 0
        for i,j in combinations(range(n),2):
            temp = len(g[i])+ len(g[j]) - (j in g[i])
            if temp>ans:
                ans = temp
                print(i,j)
        return ans