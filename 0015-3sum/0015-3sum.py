class Solution:
    def two_sum(self, arr,target):
        n = len(arr)
        if n>=2:
            d = {}
            for e in arr:
                if target-e in d.keys():
                    yield [target-e,e]
                d[e] = target-e


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        n = len(nums)
        result = set()
        nums.sort()
        for i,num1 in enumerate(nums):
            if num1<=0:
                for num2,num3 in self.two_sum(nums[i+1:],num1*-1):
                    result.add((num1,num2,num3))
            else:
                break
        return result