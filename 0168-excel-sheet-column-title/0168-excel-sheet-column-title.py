class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result =''
        while columnNumber:
            columnNumber-=1
            d = columnNumber%26
            columnNumber//=26
            result+=s[d]
        return result[::-1]