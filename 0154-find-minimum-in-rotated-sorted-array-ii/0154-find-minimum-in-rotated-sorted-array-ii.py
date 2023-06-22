class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        if n==0:
            return -5001
        if n<=5:
            return min(nums)
        f = 0
        l = n-1
        if nums[f]<nums[l]:
            return nums[f]
        mid = (l+f)//2
        if mid==0 or mid==n-1 or (nums[mid-1] > nums[mid]):
            return nums[mid]
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        if nums[f] > nums[mid] or nums[mid] > nums[l]:
            l_ans = self.findMin(nums[f:mid])
            r_ans = self.findMin(nums[mid:l+1])
            return min(l_ans,r_ans)
        if nums[f]==nums[mid]==nums[l]:
            return min(self.findMin(nums[f+1:mid]),self.findMin(nums[mid+1:l]))
        return min(nums[mid-1],nums[mid],nums[mid+1])
