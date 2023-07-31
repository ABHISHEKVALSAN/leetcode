class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def solve(str1,str2):
            n1 = len(str1)
            n2 = len(str2)
            dp = [[0] * (n2+1) for i in range(n1+1)]
            for i in range(1,n2+1):
                dp[0][i] = dp[0][i-1] + ord(str2[i-1])
            for i in range(1,n1+1):
                dp[i][0] = dp[i-1][0] + ord(str1[i-1])
            for i in range(1,n1+1):
                for j in range(1,n2+1):
                    if str1[i-1]==str2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(
                                        dp[i][j-1] + ord(str2[j-1]),
                                        dp[i-1][j] + ord(str1[i-1]))
            #print(dp)
            return dp[n1][n2]
        return solve(s1,s2)