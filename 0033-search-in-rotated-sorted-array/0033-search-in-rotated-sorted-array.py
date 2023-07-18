from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n==1:
            if target==nums[0]:
                return 0
            else:
                return -1
        end_index = None
        first = 0
        last = n-1
        while first <= last:
            mid = first + last >> 1
            if nums[mid]==target:
                return mid
            else:
                if nums[mid] > nums[last]:
                    first = mid+1
                else:
                    if mid>0 and nums[mid] < nums[mid-1]:
                        break
                    last = mid-1
        end_index = mid
        print(end_index)
        i1 = bisect_left(nums[:end_index],target)
        if i1<n and nums[i1]==target:
            return i1
        i2 = bisect_left(nums[end_index:],target)
        if i2+end_index<n and nums[end_index+i2]==target:
            return i2+end_index
        return -1
        
