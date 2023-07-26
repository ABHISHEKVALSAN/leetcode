class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_ans = float('inf')
        for i, num in enumerate(nums):
            if nums[i]==target:
                min_ans = min(min_ans, abs(i-start))
        return min_ans