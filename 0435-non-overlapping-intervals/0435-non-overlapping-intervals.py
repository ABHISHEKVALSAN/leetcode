class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n = len(intervals)
        prev = 0 
        ans = 1
        i = 1
        while i < n:
            if intervals[i][0]>=intervals[prev][1]:
                prev = i
                ans+=1
            i+=1
        return n-ans