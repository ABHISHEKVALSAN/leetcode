class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        coins.sort(reverse=True)
        dp = [0]
        for i in range(1,amount+1):
            ans = []
            for ind,coin in enumerate(coins):
                if coin == i:
                    ans.append(1)
                elif coin < i and coin <= len(dp) and dp[i-coin]!=0:
                    ans.append(dp[i-coin]+1)
            if len(ans)>0:
                dp.append(min(ans))
            else:
                dp.append(0)
        print(dp)
        if dp[amount]==0:
            return -1
        return dp[amount]
# [186,419,83,408], 6249