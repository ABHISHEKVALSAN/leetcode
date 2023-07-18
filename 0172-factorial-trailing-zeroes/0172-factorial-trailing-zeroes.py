class Solution:
    def trailingZeroes(self, n: int) -> int:
        n5 =5
        count = 0
        while n5 <= n:
            count += n//n5
            n5*=5
        return count