from heapq import heappush as hpush
from heapq import heappop as hpop
from heapq import heappushpop as hpp
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if len(self.left) > len(self.right):
            hpush(self.right,-hpp(self.left,-num))
        else:
            hpush(self.left,-hpp(self.right,num))

    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0]+self.right[0])/2.0