# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        f=1
        l=n
        mid = (f+l)//2
        while f<l:
            if isBadVersion(mid):
                l = mid-1
            elif not isBadVersion(mid):
                f = mid+1
            mid = (f+l)//2
        if isBadVersion(mid):
            return mid
        return mid+1