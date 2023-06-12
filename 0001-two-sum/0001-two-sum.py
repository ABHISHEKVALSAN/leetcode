class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        prev = {}
        for i, v in enumerate(nums):
            remaining = target - nums[i]
            if remaining in prev:
                return [i, prev[remaining]]
            
            prev[v] = i