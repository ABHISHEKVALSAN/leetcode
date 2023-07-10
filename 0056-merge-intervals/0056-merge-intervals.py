class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        if n<=1:
            return intervals
        intervals.sort()
        mi = 0
        i = 1
        while i < n:
            interval = intervals[i]
            if intervals[mi][1] < interval[0]:
                mi+=1
                intervals[mi] = interval
            else:
                if intervals[mi][1] < interval[1]:
                    intervals[mi][1]=interval[1]
            i+=1

        for i in range(mi+1,n):
            intervals.pop()
        return intervals