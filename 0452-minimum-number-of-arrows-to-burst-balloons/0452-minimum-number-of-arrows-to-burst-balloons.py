class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        result = [points[0]]
        i = 1
        n = len(points)
        while i<n:
            if result[-1][1] < points[i][0]:
                result.append(points[i])
            else:
                result[-1][0] = points[i][0]
                result[-1][1] = min(result[-1][1],points[i][1])
            i+=1
        print(result)
        return len(result)