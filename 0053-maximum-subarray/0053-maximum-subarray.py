class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        flag = True
        for num in nums:
            if num >= 0:
                flag=False
                break
        if flag:
            return max(nums)

        n = len(nums)
        i = 0
        max_sum = 0
        curr_sum = 0
        while i < n:
            if curr_sum+nums[i] <= 0:
                i+=1
                curr_sum = 0
            else:
                curr_sum+=nums[i]
                max_sum = max(max_sum, curr_sum)
                i+=1
        return max_sum