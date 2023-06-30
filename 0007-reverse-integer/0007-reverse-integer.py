class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x<0:
            sign*=-1
            x*=-1
        ans=0
        while x>0:
            r = x%10
            ans = ans*10+r
            x=x//10
        if sign==1 and ans>2**31-1:
            return 0
        if sign==-1 and ans>2**31:
            return 0
        return ans*sign
