class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for k,v in d.items():
            if v > n//2:
                return k