class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 /x
            n *= -1
            return self.myPow(x, n)
        if n==0:
            return 1.0
        elif n==1:
            return x
        elif n==2:
            return x*x
        else:
            temp = self.myPow(x,n//2)
            if n%2==0:
                return temp * temp
            else:
                return x * temp * temp 