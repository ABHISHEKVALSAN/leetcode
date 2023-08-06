from itertools import combinations, permutations
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        fact = [1,1]
        for i in range(2,n+1):
            fact.append(fact[-1]*i)
        dp = [[0 for i in range(goal+1)] for j in range(n+1)]
        for i in range(k+1, n+1):
            for j in range(i, goal+1):
                if i==j:
                    dp[i][j] = fact[i]
                else:
                    dp[i][j] = (dp[i-1][j-1] * i + dp[i][j-1] * (i-k))%(10**9+7)
        return dp[n][goal]%(10**9+7)

        