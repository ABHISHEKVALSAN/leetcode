class Solution:
    def update_mat1(self, mat, i, j):
        row, col = len(mat), len(mat[0])
        mat[i][j]=1
        if i==0:
            mat = self.update_mat2(mat, i, j)
        else:
            if mat[i-1][j]==2:
                mat = self.update_mat2(mat, i, j)
            elif j<col-1 and mat[i][j+1]==2:
                mat = self.update_mat2(mat, i, j)
            elif j>0 and mat[i][j-1]==2:
                mat = self.update_mat2(mat, i, j)
        return mat
    def update_mat2(self, mat, i, j):  
        mat[i][j] = 2
        row, col = len(mat), len(mat[0])
        if i>0 and mat[i-1][j]==1:
            mat = self.update_mat2(mat,i-1,j)
        if j>0  and mat[i][j-1]==1:
            mat = self.update_mat2(mat, i, j-1)
        if j<col-1 and mat[i][j+1]==1:
            mat =  self.update_mat2(mat, i, j+1)
        if i<row-1 and mat[i+1][j]==1:
            mat = self.update_mat2(mat, i+1, j)
        return mat
    
    def disp_mat(self, mat):
        for i in mat:
            for j in i:
                print(j,end=' ')
            print('')

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        mat = []
        for i in range(row):
            mat.append([])
            for j in range(col):
                mat[i].append(1)
        for i,j in cells:
            mat[i-1][j-1]=0
        for j in range(col):
            if mat[0][j]==1:
                mat = self.update_mat2(mat, 0, j)
        if 2 in mat[row-1]:
            return len(cells)
        while True:
            r,c = cells.pop()
            mat = self.update_mat1(mat, r-1, c-1)
            if 2 in mat[row-1]:            
                return len(cells)


        