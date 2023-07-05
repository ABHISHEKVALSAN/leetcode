class Solution:
    def is_valid_row(self, row):
        digits = ["1","2","3","4","5","6","7","8","9"]
        temp = set()
        n = 0
        for d in row:
            if d==".":
                continue
            if d not in digits:
                return False
            temp.add(d)
            n+=1
        if n != len(temp):
            return False
        return True

    def get_cell(self, board, r, c):
        temp = []
        for i in range(r,r+3):
            for j in range(c,c+3):
                temp.append(board[i][j])
        return temp

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid_row(row):
                return False
        i = 0
        while i < 9:
            j = 0
            temp = []
            while j < 9:
                temp.append(board[j][i])
                j+=1
            if not self.is_valid_row(temp):
                return False
            i+=1
        
        for i in [0,3,6]:
            for j in [0,3,6]:
                row = self.get_cell(board,i,j)
                if not self.is_valid_row(row):
                    return False
        return True 