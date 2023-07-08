class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        curr_min = 0
        curr_max = 0
        _sum = 0
        for num in nums:
            curr_max = max(curr_max, 0) + num
            max_sum = max(curr_max, max_sum)
            curr_min = min(curr_min, 0) + num
            min_sum = min(min_sum, curr_min)
            _sum += num
        return max_sum if min_sum==_sum else max(max_sum, _sum-min_sum)

