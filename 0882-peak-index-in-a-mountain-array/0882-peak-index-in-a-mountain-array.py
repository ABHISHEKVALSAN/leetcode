class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left  = 0
        right = len(arr)-1
        mid = (left+right)>>1
        while left < right:
            if arr[mid]>arr[left] and arr[mid]<=arr[right]:
                left = mid
            elif arr[mid] > arr[right] and arr[mid]<=arr[left]:
                right = mid
            else:
                left+=1
            mid = (left+right)>>1
        return mid