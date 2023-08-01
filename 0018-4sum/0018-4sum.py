from ast import literal_eval
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        def two_sum(arr,target):
            d = set([])
            for i in arr:
                if target-i in d:
                    yield [i,target-i]
                d.add(i)
        def three_sum(arr,target):
            for i,e in enumerate(arr):
                for ans in two_sum(arr[i+1:],target-e):
                    yield [e]+ans
        nums.sort()
        for i,e in enumerate(nums):
            for ans in three_sum(nums[i+1:],target-e):
                temp = [e]+ans
                temp.sort()
                result.add(str(temp))
        return [literal_eval(i) for i in result]