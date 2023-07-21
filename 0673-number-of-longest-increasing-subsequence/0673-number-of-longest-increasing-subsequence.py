class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1 for num in nums]
        freq = [1 for num in nums]
        n = len(nums)
        i = 1
        mx = 1
        while i < n:
            j = 0
            while j<i:
                if nums[i] > nums[j]:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        freq[i] = freq[j]
                    elif dp[j]+1==dp[i]:
                        freq[i]+=freq[j]
                j+=1
            mx = max(mx,dp[i])
            i+=1
        print(dp)
        print(freq)
        result = 0 
        for i in range(n):
            if dp[i]==mx:
                result+=freq[i]
        return result
        
        