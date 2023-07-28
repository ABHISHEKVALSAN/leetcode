class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        s1 = list(s1)
        s2 = list(s2)
        s3 = list(s3)
        def solve(str1,str2,str3):
            s = str([str1,str2,str3])
            if s in dp:
                return dp[s]
            if len(str1)+len(str2)!=len(str3):
                dp[s] = False
                return dp[s]
            if len(str1)==len(str2)==len(str3)==0:
                dp[s] = True
                return dp[s]
            if len(str1)==0:
                if str2==str3:
                    dp[s] = True
                    return dp[s]
                else:
                    dp[s] = False
                    return dp[s]
            if len(str2)==0:
                if str1==str3:
                    dp[s] = True
                    return dp[s]
                else:
                    dp[s] = False
                    return dp[s]
            if str1[-1]==str3[-1] and str2[-1]==str3[-1]:
                dp[s] = solve(str1[:-1],str2,str3[:-1]) or solve(str1,str2[:-1],str3[:-1])
                return dp[s]
            elif str1[-1]==str3[-1]:
                dp[s] = solve(str1[:-1],str2,str3[:-1])
                return dp[s]
            elif str2[-1]==str3[-1]:
                dp[s] = solve(str1,str2[:-1],str3[:-1])
                return dp[s]
            else:
                dp[s] = False
                return dp[s]
        return solve(s1,s2,s3)