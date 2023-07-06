class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        for num in nums:
            if num>=target:
                return 1
        if sum(nums) < target:
            return 0
        i = 0
        j = 1
        s = nums[0]
        ml = n
        while i < j and j < n:
            s += nums[j]
            while i < j and s >= target:
                ml = min(ml, j - i + 1)
                s -= nums[i]
                i+=1
            j+=1
        return ml