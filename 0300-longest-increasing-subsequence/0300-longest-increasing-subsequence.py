from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lss = [nums[0]]
        for num in nums[1:]:
            if num>lss[-1]:
                lss.append(num)
            else:
                lss[bisect_left(lss,num)] = num
        return len(lss)