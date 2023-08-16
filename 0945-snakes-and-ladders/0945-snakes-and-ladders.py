from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def conv_ij(pos):
            pos-=1
            i = n-(pos//n)-1
            j = pos%(n*2) if pos%(n*2) < n else n*2-(pos%(n*2))-1
            return i,j
        
        def bfs(a):
            queue = deque()
            vis = set()
            queue.append((a,0))
            vis.add(a)
            while queue:
                curr_pos, step = queue.popleft()
                if curr_pos==n*n:
                    return step
                for dice_value in range(1,7):
                    next_pos = curr_pos + dice_value
                    if next_pos==n*n:
                        return step+1
                    i, j = conv_ij(next_pos)
                    if board[i][j]!=-1:
                        next_pos = board[i][j]
                        if next_pos==n*n:
                            return step+1
                    if next_pos not in vis:
                        vis.add(next_pos)
                        queue.append((next_pos,step+1))
            return -1
        return bfs(1)
