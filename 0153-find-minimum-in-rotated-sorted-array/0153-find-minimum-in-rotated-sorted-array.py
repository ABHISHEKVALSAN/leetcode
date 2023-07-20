class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 0 
        last = len(nums)-1
        mid = (first + last)//2
        while first<last:
            
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            else:
                if nums[first]<nums[mid]<nums[last]:
                    last=mid-1
                elif nums[first]<nums[mid]>nums[last]:
                    first = mid+1
                elif nums[first]>nums[mid]<nums[last]:
                    last = mid-1
                else:
                    first+=1
            mid = (first + last)//2
        return min(nums[mid],nums[mid-1])