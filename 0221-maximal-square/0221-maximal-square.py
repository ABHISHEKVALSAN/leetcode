class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        if row == 1:
            if "1" not in matrix[0]:
                return 0
            else:
                return 1
        if col == 1:
            for i in range(row):
                if matrix[i][0]=="1":
                    return 1
            return 0
        max_sq = 0
        for i in range(row):
            if matrix[i][0]=="1":
                max_sq=1
                break
        if max_sq == 0:
            for i in range(col):
                if matrix[0][i]=="1":
                    max_sq=1
                    break
        
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]=="1":
                    matrix[i][j] = str(min(
                                        int(matrix[i-1][j-1]),
                                        int(matrix[i-1][j]),
                                        int(matrix[i][j-1])) + 1)
                    max_sq = max(max_sq, int(matrix[i][j]))
        return max_sq * max_sq