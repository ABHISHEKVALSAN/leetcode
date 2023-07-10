class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        intervals.sort()
        for interval in intervals:
            if len(merged_intervals)==0:
                merged_intervals.append(interval)
            else:
                if merged_intervals[-1][1] < interval[0]:
                    merged_intervals.append(interval)
                else:
                    if merged_intervals[-1][1] < interval[1]:
                        merged_intervals[-1][1]=interval[1]
        return merged_intervals