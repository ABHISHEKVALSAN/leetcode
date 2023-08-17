class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        from_left = 0
        from_top = 0
        for i in range(row):
            for j in range(col):
                if j==0:
                    if grid[i][j]==1:
                        from_left+=1
                elif grid[i][j-1]==0 and grid[i][j]==1:
                    from_left+=1
                if i==0:
                    if grid[i][j]==1:
                        from_top+=1
                elif grid[i-1][j]==0 and grid[i][j]==1:
                    from_top+=1
        return 2*(from_left+from_top)
