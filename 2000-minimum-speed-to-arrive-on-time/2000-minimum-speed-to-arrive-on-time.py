import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def solve(s):
            time_taken = 0
            for i, d in enumerate(dist):
                t = float(d)/s
                time_taken+= math.ceil(t) if i!=len(dist)-1 else t
                if time_taken>hour:
                    return False
            return time_taken<=hour
        if hour <= len(dist)-1:
            return -1
        elif len(dist)-1<hour<=len(dist):
            speed = round(float(hour) - float(len(dist)) + 1.0,5)
            print(speed)
            return  max(max(dist), math.ceil(dist[-1]/speed))
        else:
            if hour >= sum(dist):
                return 1
            min_speed = -1
            first, last = 1, max(dist)
            while first<=last:
                mid = (first+last)//2
                if solve(mid):
                    min_speed = mid
                    last = mid-1
                else:
                    first = mid+1
            return min_speed
            