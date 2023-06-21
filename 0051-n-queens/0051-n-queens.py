class Solution:
    def is_complete_board(self,board):
        n = len(board)
        for i in range(n):
            if 'Q' not in board[i]:
                return False
        return True

    def is_valid(self, board, r, c):
        n = len(board)
        if board[r][c]=='Q':
            return False
        for i in range(n):
            if r-i >=0 and c-i>=0 and board[r-i][c-i]=='Q':
                return False
            elif r-i >=0 and board[r-i][c]=='Q':
                return False
            elif r-i >=0 and c+i < n and board[r-i][c+i]=='Q':
                return False
            elif r+i < n and c-i>=0 and board[r+i][c-i]=='Q':
                return False
            elif r+i < n and board[r+i][c]=='Q':
                return False
            elif r+i < n and c+i < n and board[r+i][c+i]=='Q':
                return False
            elif c-i >=0 and board[r][c-i]=='Q':
                return False
            elif c+i < n and board[r][c+i]=='Q':
                return False
        return True

    def solve(self, board, r):
        if self.is_complete_board(board):
            yield board
        else:
            n = len(board)
            for i in range(n):
                if self.is_valid(board, r, i):
                    board[r][i]='Q'
                    for b in self.solve(board,r+1):
                        yield b
                    board[r][i]='.'

        
    def solveNQueens(self, n: int) -> List[List[str]]:
        b = []
        for i in range(n):
            b.append(list('.'*n))
        result = []
        for board in self.solve(b,0):
            nb = []
            for x in board:
                nb.append(''.join(x))
            result.append(nb)
        return result