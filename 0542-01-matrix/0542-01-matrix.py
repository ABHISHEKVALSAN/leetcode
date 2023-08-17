from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        vis = set()
        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    vis.add((i,j))
                    queue.append((i,j,0))
        while queue:
            i, j, val = queue.popleft()
            mat[i][j] = val
            if i > 0 and (i-1,j) not in vis:
                vis.add((i-1,j))
                queue.append((i-1,j,val+1))
            if j > 0 and (i,j-1) not in vis: 
                vis.add((i,j-1))
                queue.append((i,j-1,val+1))
            if i<row-1 and (i+1,j) not in vis:
                vis.add((i+1,j))
                queue.append((i+1,j,val+1))
            if j<col-1 and (i,j+1) not in vis:
                vis.add((i,j+1))
                queue.append((i,j+1,val+1))
        return mat