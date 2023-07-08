class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n > 0:
            d = n%2
            if d==1:
                num+=1
            n //=2

        return num