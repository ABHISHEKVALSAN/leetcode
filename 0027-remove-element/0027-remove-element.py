class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        for i,e in enumerate(nums):
            if e==val:
                nums[i]='_'
        
        i = 0
        ui = 0
        n = len(nums)
        while i < n:
            if nums[i]!='_':
                nums[ui]=nums[i]
                ui+=1
            i+=1
        return ui
