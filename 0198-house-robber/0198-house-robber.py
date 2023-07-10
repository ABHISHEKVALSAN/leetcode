class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums))]
        def solve(nums,i):
            if dp[i]!=-1:
                return dp[i]
            n = len(nums)
            if n==0:
                return 0
            elif n==1:
                return nums[0]
            elif n==2:
                return max(nums)
            else:
                dp[i] = max(solve(nums[1:],i+1),nums[0]+solve(nums[2:],i+2))
            return dp[i]
        return solve(nums,0)
