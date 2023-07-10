class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n = columnNumber
        result = ''
        while n>0:
            n-=1
            d = n%26
            result+=s[d]
            n//=26
        return result[::-1]



        return result[::-1]
