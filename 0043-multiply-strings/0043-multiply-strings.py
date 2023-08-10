class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        n1 = n2 = 0
        for ch in num1:
            n1 = n1*10 + int(ch)
        for ch in num2:
            n2 = n2*10 + int(ch)
        result = '' 
        num = n1*n2
        while num:
            d = num%10
            result+=str(d)
            num//=10
        return result[::-1]
