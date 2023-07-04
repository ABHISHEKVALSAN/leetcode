class Solution:
    def __init__(self):
        self.arr = [-1 for _ in range(45)]
        self.arr[0] = 1
        self.arr[1] = 2
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            if self.arr[n-1-1]==-1:
                s1 = self.climbStairs(n-1) 
                self.arr[n-1-1]=s1
            if self.arr[n-2-1]==-1:
                s2 = self.climbStairs(n-2)
                self.arr[n-2-1]=s3
            return self.arr[n-1-1]+self.arr[n-2-1]

            