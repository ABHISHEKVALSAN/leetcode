class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp = [1 for _ in pairs]
        pairs.sort()
        n = len(pairs)
        i = 0
        while i<n-1:
            j = i+1
            while j<n:
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j],dp[i]+1)
                j+=1
            i+=1
        return dp[-1]