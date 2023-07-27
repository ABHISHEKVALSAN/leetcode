from heapq import heappush as hpush, heappop as hpop
from collections import deque
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        s = sum(batteries)
        i = len(batteries)-1
        while i>=0 and s//n < batteries[i]:
            s-=batteries[i]
            n-=1
            i-=1
        return s//n