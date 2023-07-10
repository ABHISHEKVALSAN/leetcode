class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]
        n = len(nums)
        i = 1
        while i < n:
            j = 0
            while j < i:
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
                j+=1
            i+=1
        return max(dp)