class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        elif n>=2:
            if nums[0] > nums[1]:
                return 0
            elif nums[-1] > nums[-2]:
                return n-1
        first = 0
        last = n-1
        while first < last:
            mid = (first + last )//2
            if mid > 0 and mid < n-1 and nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[first] >= nums[mid]:
                last = mid
            elif nums[last] > nums[mid]:
                first = mid
            else:
                first+=1
        return mid

            