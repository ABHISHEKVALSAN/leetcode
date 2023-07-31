class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        n =len(nums)
        if n==0:
            return 0
        max_ans = 1
        ans = 1
        i = 0
        while i<n-1:
            if nums[i]+1==nums[i+1]:
                ans+=1
                max_ans = max(max_ans,ans)
            else:
                ans = 1
            i+=1
        return max_ans