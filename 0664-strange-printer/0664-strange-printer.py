class Solution:
    def strangePrinter(self, s: str) -> int:
        def mod_string(s):
            curr = ''
            result = ''
            for ch in s:
                if ch==curr:
                    continue
                else:
                    curr = ch
                    result+=ch
            return result
        def solve(s):
            s = mod_string(s)
            n = len(s)
            dp = [[0]*n for _ in range(n)]
            i = n-1
            while i>=0:
                dp[i][i] =1
                j = i+1
                while j < n:
                    dp[i][j] = dp[i][j-1]+1
                    k = i
                    while k<j:
                        if s[k]==s[j]:
                            if k+1 <= j-1:
                                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j-1])
                            else:
                                dp[i][j] = min(dp[i][j],dp[i][k])
                        k+=1
                    j+=1
                i-=1
            return dp[0][n-1]
        return solve(s)

