class Solution:
    def is_board_complete(self, board):
        for i in range(8,-1,-1):
            for j in range(8,-1,-1):
                if board[i][j]==".":
                    return False
        return True

    def validate_insert(self, board, r, c, d):
        for i in range(9):
            if i!=r:
                if board[i][c]==str(d):
                    return False
        for j in range(9):
            if j!=c:
                if board[r][j]==str(d):
                    return False
        l1 = [0,1,2]
        l2 = [3,4,5]
        l3 = [6,7,8]

        if r in l1 and c in l1:
            for r1 in l1:
                for c1 in l1: 
                    if r1==r and c1==c:
                        continue
                    if board[r1][c1]==str(d):
                        return False    
        if r in l1 and c in l2:
            for r1 in l1:
                for c1 in l2: 
                    if r1==r and c1==c:
                        continue
                    if board[r1][c1]==str(d):
                        return False   
        if r in l1 and c in l3:
            for r1 in l1:
                for c1 in l3: 
                    if r1==r and c1==c:
                        continue
                    if board[r1][c1]==str(d):
                        return False
        if r in l2 and c in l1:
            for r1 in l2:
                for c1 in l1: 
                    if r1==r and c1==c:
                        continue
                    if board[r1][c1]==str(d):
                        return False
        if r in l2 and c in l2:
            for r1 in l2:
                for c1 in l2: 
                    if r1==r and c1==c:
                        continue
                    if board[r1][c1]==str(d):
                        return False
        if r in l2 and c in l3:
            for r1 in l2:
                for c1 in l3: 
                    if r1==r and c1==c:
                        continue
                    if board[r1][c1]==str(d):
                        return False
        if r in l3 and c in l1:
            for r1 in l3:
                for c1 in l1: 
                    if r1==r and c1==c:
                        continue
                    if board[r1][c1]==str(d):
                        return False
        if r in l3 and c in l2:
            for r1 in l3:
                for c1 in l2: 
                    if r1==r and c1==c:
                        continue
                    if board[r1][c1]==str(d):
                        return False
        if r in l3 and c in l3:
            for r1 in l3:
                for c1 in l3: 
                    if r1==r and c1==c:
                        continue
                    if board[r1][c1]==str(d):
                        return False

        return True
    def solve(self, board):

        if self.is_board_complete(board)==True:
            return board, True

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    for d in range(1,10):
                        if self.validate_insert(board,i,j,d):
                            board[i][j]=str(d)
                            board, state = self.solve(board)
                            if state==True:
                                return board, True
                            board[i][j]="."
                    return board, False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board, state = self.solve(board)
