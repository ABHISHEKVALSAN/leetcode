class Solution:
    def is_complete(self, board):
        n = len(board)
        for i in range(n):
            if sum(board[i])!=1:
                return False
        return True
    
    def is_valid(self, board, r, c):
        n = len(board)
        if board[r][c]==1:
            return False
        for i in range(n):
            if r-i >= 0 and c-i >= 0 and board[r-i][c-i]==1:
                return False
            elif r-i >= 0 and board[r-i][c]==1:
                return False
            elif r-i >= 0 and c+i < n and board[r-i][c+i]==1:
                return False
            elif c-i >= 0 and board[r][c-i]==1:
                return False
            elif c+i < n and board[r][c+i]==1:
                return False
            elif r+i < n and c-i >= 0 and board[r+i][c-i]==1:
                return False
            elif r+i < n and board[r+i][c]==1:
                return False
            elif r+i < n and c+i < n and board[r+i][c+i]==1:
                return False
        return True
    
    def solve(self,board,r):
        if self.is_complete(board):
            yield board
        else:
            n = len(board)
            for i in range(n):
                if self.is_valid(board, r, i):
                    board[r][i] = 1
                    for board in self.solve(board,r+1):
                        yield board
                    board[r][i] = 0
    def totalNQueens(self, n: int) -> int:
        b = []
        for i in range(n):
            b.append([0 for _ in range(n)])

        ans = 0
        for board in self.solve(b,0):
            ans+=1
        return ans
