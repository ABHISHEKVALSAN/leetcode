class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        mul = 1
        num = 0
        while n>0:
            d = n%10
            n//=10
            num = d*mul + num
            if d==0:
                ans+=(n*mul)
            elif ans!=0 and d==1:
                ans+=(num+1)
                ans+=((n-1)*mul)
            else:
                ans+=((n+1)*mul)
            mul*=10
        return ans
