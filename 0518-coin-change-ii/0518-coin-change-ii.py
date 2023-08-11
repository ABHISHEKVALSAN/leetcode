class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount==0:
            return 1
        if len(coins)==1:
            return int(amount%coins[0]==0)
        coins.sort()
        dp = [[0 for i in range(amount+1)] for coin in coins]
        for i in range(1,amount+1):
            if i%coins[0]==0:
                dp[0][i]=1
        for i in range(len(coins)):
            for j in range(1,amount+1):
                dp[i][j] = int(j%coins[i]==0) + sum([dp[i-1][k] for k in range(j,-1,-coins[i])])
        print(dp)
        return dp[-1][-1]