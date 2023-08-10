from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def get_small_index(arr):
            first, last = 0, len(arr)-1
            while first<last:
                mid = (first+last)//2
                if mid > 0 and arr[mid] < arr[mid-1]:
                    return mid
                if mid < len(arr)-1 and arr[mid] > arr[mid+1]:
                    return mid+1
                if arr[mid]==arr[last]:
                    if arr[mid] == arr[first]:
                        first+=1
                    else:
                        last = mid
                elif arr[mid] > arr[last]:
                    first = mid + 1
                else:
                    last = mid
            return first
        n = len(nums)
        small_index = get_small_index(nums)
        print(small_index)
        i1 = bisect_left(nums[:small_index],target)
        s1 = i1 < small_index and nums[:small_index][i1]==target
        i2 = bisect_left(nums[small_index:],target)
        s2 = i2 < len(nums[small_index:]) and nums[small_index:][i2]==target
        return s1 or s2
        
