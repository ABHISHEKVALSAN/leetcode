import math
from collections import deque
class Solution:

    def soupServings(self, n: int) -> float:
        
        def solve(a,b):
            if dp[a][b]!=-1:
                return dp[a][b]
            if a==0:
                if b==0:
                    return 0.5
                else:
                    return 1
            elif b==0:
                return 0
            else:
                p1 = solve(max(0,a-4),b)
                p2 = solve(max(0,a-3),max(0,b-1))
                p3 = solve(max(0,a-2),max(0,b-2))
                p4 = solve(max(0,a-1),max(0,b-3))
                dp[a][b] = 0.25*(p1+p2+p3+p4)
                return dp[a][b]
        if n > 4500:
            return 1.0
        n = math.ceil(n/25)
        dp = []
        for i in range(n+1):
            dp.append([])
            for j in range(n+1):
                dp[i].append(-1)
        return solve(n,n)