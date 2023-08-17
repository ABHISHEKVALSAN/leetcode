class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x^y
        hd = 0
        while n:
            n&=(n-1)
            hd+=1
        return hd