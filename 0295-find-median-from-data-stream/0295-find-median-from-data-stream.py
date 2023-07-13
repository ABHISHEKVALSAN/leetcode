from bisect import bisect_left
class MedianFinder:

    def __init__(self):
        self.is_odd = False
        self.arr = []
        self.last_sort_index = 0
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)


    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)
        if n%2==1:
            return self.arr[n//2]
        else:
            return (self.arr[n//2] + self.arr[(n//2)-1])/2.0