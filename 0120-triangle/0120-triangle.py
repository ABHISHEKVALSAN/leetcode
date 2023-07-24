class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        I = n-2
        while I>=0:
            for ind, e in enumerate(triangle[I]):
                triangle[I][ind] = e + min(triangle[I+1][ind],triangle[I+1][ind+1]) 
            I-=1
        return triangle[0][0]