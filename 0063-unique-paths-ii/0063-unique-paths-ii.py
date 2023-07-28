class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r,c = len(obstacleGrid), len(obstacleGrid[0])
        def solve(i,j):
            if obstacleGrid[i][j]==1:
                return False
            if obstacleGrid[i][j]==2:
                return True
            if i==0 and j==0:
                obstacleGrid[i][j] = 2
                return True
            
            if obstacleGrid[i][j]==0:
                flag = False
                if i>0 and solve(i-1,j):
                    flag = True
                    obstacleGrid[i-1][j] = 2
                if j>0 and solve(i,j-1):
                    flag = True
                    obstacleGrid[i][j-1] = 2
                    return True
                return flag
        if solve(r-1,c-1):
            obstacleGrid[r-1][c-1]=2
        if obstacleGrid[0][0]!=2:
            return 0
        for i in range(r):
            for j in range(c):
                obstacleGrid[i][j] = 1 if obstacleGrid[i][j]==2 else 0
        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        print(obstacleGrid)
        return obstacleGrid[r-1][c-1]