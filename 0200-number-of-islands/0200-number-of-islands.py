class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def spread(grid,r,c,i,j,num):
            grid[i][j] = num
            if i>0 and grid[i-1][j]==1:
                spread(grid,r,c,i-1,j,num)
            if j>0 and grid[i][j-1]==1:
                spread(grid,r,c,i,j-1,num)
            if i<r-1 and grid[i+1][j]==1:
                spread(grid,r,c,i+1,j,num)
            if j<c-1 and grid[i][j+1]==1:
                spread(grid,r,c,i,j+1,num)
        row, col = len(grid), len(grid[0])
        total = 2
        for i in range(row):
            for j in range(col):
                grid[i][j] = int(grid[i][j])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    spread(grid,row,col,i,j,total)
                    total+=1
        return total-2

