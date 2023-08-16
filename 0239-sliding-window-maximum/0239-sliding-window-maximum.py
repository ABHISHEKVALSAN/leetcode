from heapq import heappush as hpush, heappop as hpop,heappushpop as hpp
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0 
        h = []
        while i<k:
            hpush(h,(-nums[i],i))
            i+=1
        result = [-h[0][0]]
        n = len(nums)
        while i < n:
            hpush(h, (-nums[i],i))
            while h[0][1] <= i-k:
                hpop(h)
            result.append(-h[0][0])
            i+=1
        return result