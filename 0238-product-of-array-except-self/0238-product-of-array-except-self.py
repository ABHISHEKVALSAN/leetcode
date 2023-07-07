class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>=2:
            return [0 for num in nums]
        elif nums.count(0)==1:
            result = [0 for num in nums]
            index = nums.index(0)
            p = 1
            for i,e in enumerate(nums):
                if i==index:
                    continue
                p*=e
            result[index] = p
            return result
        else:
            p = 1
            for num in nums:
                p*=num
            result = [p for _ in nums]
            for i,num in enumerate(nums):
                result[i]//=num
            return result