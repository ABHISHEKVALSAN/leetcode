class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        while i < n:
            if i < n-2 and nums[i] == nums[i+2]:
                i+=1
            else:
                nums[j] = nums[i]
                i+=1
                j+=1
        return j


