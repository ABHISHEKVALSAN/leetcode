import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 1
        n = len(numbers)
        while i < n:
            if numbers[i-1]+numbers[i]==target:
                return [i,i+1]
            i+=1
        i=0
        while i<n:
            num = numbers[i]
            ind = bisect.bisect_left(numbers, target-num)
            if ind>=0 and ind<n and ind!=i and numbers[ind]==target-num:
                return [i+1,ind+1]
            i+=1

