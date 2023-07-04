class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target > nums[n-1]:
            return n
        elif target==nums[n-1]:
            return n-1
        if target <= nums[0]:
            return 0
        
        first = 0
        last = n-1
        while first<=last:
            mid = (first+last)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                last = mid - 1
            elif target > nums[mid]:
                first = mid + 1
        if nums[mid]>target:
            return mid
        return mid+1
