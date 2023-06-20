class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = int(int(dividend) / int(divisor))
        if ans > 2**31 - 1:
            return 2**31 - 1
        if ans < -1 * 2**31:
            return -1 * 2**31
        print(dividend,divisor,ans)
        return ans