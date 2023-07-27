class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        n = len(nums)
        while i < n-1 and j<n:
            if nums[i]==0 and nums[j]==0:
                j+=1
            elif nums[j]==0:
                i+=1
            elif nums[i]==0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            else:
                i+=1
                j+=1
        if nums[i]==0:
            nums[i],nums[-1] = nums[-1],nums[i]