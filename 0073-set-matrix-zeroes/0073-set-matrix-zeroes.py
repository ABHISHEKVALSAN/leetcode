class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def spread(i,j):
            for k in range(r):
                if matrix[k][j]==0:
                    continue
                elif matrix[k][j]==0.5:
                    break
                elif matrix[k][j]==0.75:
                    break
                elif matrix[k][j]==0.25:
                    matrix[k][j]=0.5
                else:
                    matrix[k][j]=0.75
            for k in range(c):
                if matrix[i][k]==0:
                    continue
                elif matrix[i][k]==0.5:
                    break
                elif matrix[i][k]==0.25:
                    break
                elif matrix[i][k]==0.75:
                    matrix[i][k]=0.5
                else:
                    matrix[i][k]=0.25
                    
        r, c = len(matrix),len(matrix[0])
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    spread(i,j)
        print(matrix)
        for i in range(r):
            for j in range(c):
                if 0<matrix[i][j]<1:
                    matrix[i][j]=0
                    