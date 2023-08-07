class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(i,j,index):
            if i<0 or j<0 or i>=row or j>=col:
                return False
            if word[index] == board[i][j]:
                if index==len(word)-1:
                    return True
                board[i][j] = index
                status = solve(i+1,j,index+1) or \
                         solve(i-1,j,index+1) or \
                         solve(i,j-1,index+1) or \
                         solve(i,j+1,index+1)
                board[i][j] = word[index]
                return status
            else:
                return False
        
        row, col = len(board), len(board[0])
        for r in range(row):
            for c in range(col):
                if solve(r,c,0):
                    return True
        return False