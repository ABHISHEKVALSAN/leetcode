class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = -101
        for i,e in enumerate(nums):
            if curr==e:
                nums[i]='_'
            else:
                curr = e
        i = 0
        ui = 0
        n = len(nums)
        while i < n:
            if nums[i]!='_':
                nums[ui] = nums[i]
                ui+=1
            i+=1
        return ui



        