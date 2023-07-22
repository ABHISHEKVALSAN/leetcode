class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def get_value(r,c):
            if r<n and c<n and r>=0 and c>=0:
                return dp[r][c]
            else:
                return 0
        def update(dp):
            dp_new = []
            for i in range(n):
                dp_new.append([])
                for j in range(n):
                    dp_new[i].append(dp[i][j])

            direction = [[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2]]
            for i in range(n):
                for j in range(n):
                    prob = []
                    for rd,cd in direction:
                        val = get_value(i+rd,j+cd)
                        #print(k,i,j,val)
                        prob.append(val)
                    dp_new[i][j] = sum(prob)/8
            return dp_new
        dp = []
        for i in range(n):
            dp.append([])
            for j in range(n):
                dp[i].append(1)
        for i in range(k):
            dp = update(dp)
        return dp[row][column]
            

