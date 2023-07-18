class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_live(i,j):
            if board[i][j] in [0,3]:
                return False
            return True
        def get_count(i,j):
            d = [[0,1],[1,0],[0,-1],[-1,0],[1,-1],[-1,1],[1,1],[-1,-1]]
            count = 0
            for ad in d:
                if i+ad[0] >= 0 and i+ad[0]< r and j+ad[1]>=0 and j+ad[1]<c:
                    count+=int(is_live(i+ad[0],j+ad[1]))
            return count

        
        r = len(board)
        c = len(board[0])
        #print(board,r,c)
        for i in range(r):
            for j in range(c):
                count = get_count(i,j)
                if is_live(i,j) and (count<2 or count>3):
                    board[i][j]=2
                if not is_live(i,j) and count==3:
                    board[i][j]=3
        for i in range(r):
            for j in range(c):
                #print(i,j)
                board[i][j] = (board[i][j])%2
                