class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        ans = 0
        while i < n:
            ans = ans ^ nums[i]
            i+=1
        return ans