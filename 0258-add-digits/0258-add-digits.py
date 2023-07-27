class Solution:
    def addDigits(self, num: int) -> int:
        
        if num<10:
            return num
        n = 0
        while num>0:
            n += num%10
            num//=10
        return self.addDigits(n)