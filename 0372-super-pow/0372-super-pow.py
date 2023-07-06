class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def my_pow(x, n):
            x = x%1337
            if n==0:
                return 1
            elif n==1:
                return x
            else:
                temp = my_pow(x,n//2)
                temp = (temp * temp) % 1337
                if n%2==0:
                    return temp
                else:
                    return (x*temp)%1337
        a = a%1337
        if len(b)==0:
            return 1
        bl = b.pop()
        return (my_pow(self.superPow(a,b),10) * my_pow(a,bl))%1337
        