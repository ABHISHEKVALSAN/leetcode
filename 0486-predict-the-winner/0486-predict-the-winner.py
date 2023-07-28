class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = []
        n = len(nums)
        for i in range(n):
            dp.append([])
            for j in range(n):
                dp[i].append(0)
        
        def solve(i,j):
            if i>j:
                return 0
            n = j-i+1
            if dp[i][j]!=0:
                return dp[i][j]
            if n==1:
                dp[i][j]=nums[i]
                return dp[i][j]
            elif n==2:
                dp[i][j] = max(nums[i:j+1])
                return dp[i][j]
            elif n==3:
                dp[i][j] = max(
                                nums[i] + min(nums[i+1:j+1]), 
                                nums[j] + min(nums[i:j-1]))
                return dp[i][j]
            else:
                dp[i][j] = max(
                                nums[i]+ min(solve(i+2,j),solve(i+1,j-1)),
                                nums[j]+ min(solve(i+1,j-1),solve(i,j-2)))
                return dp[i][j]
        p1_sum = solve(0,n-1)
        print(dp)
        if p1_sum < sum(nums)/2:
            return False
        return True
        