from collections import deque
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def solve(arr, index, p):
            n = len(nums)
            i = 0
            c = 0
            while i < n-1:
                if nums[i+1] - nums[i] <= index:
                    c+=1
                    i+=1
                if c>=p:
                    return True
                i+=1
            return False
        nums.sort()
        n = len(nums)
        f, l = 0, nums[-1] - nums[0]
        while f < l:
            mid = (f+l)>>1
            if solve(nums, mid, p):
                l = mid
            else:
                f = mid + 1
        return f

'''[75841,10836,90297,65300,2691,4222,31819,62366,74592,61726,2747,25749,82186,13526,68417,20213,51542,53629,48677,39515,1420,29980,82925,28030,48133,8712,18133,58186,90944,14106,58497,7113,22120,37507,8118,34489,55965,48887,18831,17644,77696,23889,705,28242,76776]'''