class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        curr_sp = 1
        for i,e in enumerate(nums):
            if e<=0:
                continue
            if i < n-1 and nums[i]==nums[i+1]:
                continue
            if e==curr_sp:
                curr_sp+=1
            else:
                break
        return curr_sp
        