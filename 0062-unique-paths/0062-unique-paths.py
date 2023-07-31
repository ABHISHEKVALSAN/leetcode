class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def get_row(r,ind):
            prev = 1
            for i in range(min(r-1,ind)-1):
                curr = prev * (r-i-1) / (i+1)
                prev = curr
            return curr
        if m==1 or n==1:
            return 1
        r = m + n -1
        row = get_row(r,min(m,n))
        return int(row)
