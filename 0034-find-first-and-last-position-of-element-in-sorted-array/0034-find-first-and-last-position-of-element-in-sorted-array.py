from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = bisect_left(nums,target)
        r = bisect_right(nums,target)
        print(l,r)
        if l<n and r-1<n and nums[l]==target and nums[r-1]==target:
            return [l,r-1]
        return [-1,-1]