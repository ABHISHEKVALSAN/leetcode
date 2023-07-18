class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result_intervals = []
        i = 0
        n = len(intervals)
        if n==0 or newInterval[0] > intervals[n-1][1]:
            intervals.append(newInterval)
            return intervals
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
         
        i = 0
        while i < n-1:
            if intervals[i][1] < newInterval[0] and newInterval[1]<intervals[i+1][0]:
                return intervals[:i+1] + [newInterval] + intervals[i+1:]
            i+=1
        i=0
        while i<n:
            if newInterval[0] <= intervals[i][1]:
                if i==0 or newInterval[0] > intervals[i-1][1]:
                    intervals[i][0] = min(newInterval[0],intervals[i][0])
                intervals[i][1] = max(newInterval[1], intervals[i][1])
                break
            i+=1
        if i==n:
            intervals.append(newInterval)
            return intervals
        new_int = intervals[i]
        i+=1
        while i<n:
            if new_int[1] >= intervals[i][0]:
                if new_int[1] < intervals[i][1]:
                    new_int[1] = intervals[i][1]
                intervals[i] = []
                i+=1
            else:
                break
        return [i for i in intervals if i!=[]]