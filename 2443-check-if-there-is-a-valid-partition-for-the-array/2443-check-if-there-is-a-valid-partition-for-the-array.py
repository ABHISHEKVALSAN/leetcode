class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = {}
        n = len(nums)
        def solve(i):
            if i in dp:
                return dp[i]
            if i>=n:
                dp[i] = True
                return dp[i]
            if i==n-1:
                dp[i]= False
                return False
            elif i==n-2:
                dp[i] = nums[i]==nums[i+1]
                return dp[i]
            elif i==n-3:
                dp[i] = nums[i]==nums[i+1]==nums[i+2] or \
                        nums[i]+2==nums[i+1]+1==nums[i+2]
                return dp[i]
            elif i<n-3:
                if nums[i]==nums[i+1] and solve(i+2):
                    dp[i] = True
                    return dp[i]
                if nums[i]==nums[i+1]==nums[i+2] and solve(i+3):
                    dp[i] = True
                    return dp[i]
                if nums[i]+2==nums[i+1]+1==nums[i+2] and solve(i+3):
                    dp[i] = True
                    return dp[i]
                dp[i] = False
                return dp[i]
        return solve(0)