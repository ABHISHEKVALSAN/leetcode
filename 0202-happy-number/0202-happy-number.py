class Solution:
    def isHappy(self, n: int) -> bool:
        def solve(number):
            ans = 0
            while number>0:
                d = number%10
                ans+= d*d
                number//=10
            return ans
        if n==1:
            return True
        slow = n
        fast = solve(n)
        while slow!=fast:
            print(slow,fast)
            if slow==1 or fast==1:
                return True
            slow = solve(slow)
            fast = solve(solve(fast))
        return False