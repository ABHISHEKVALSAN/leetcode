class Solution:
    def canCross(self, stones: List[int]) -> bool:
        last_stone = stones[-1]
        d = {}
        def solve(pos,k):
            if (pos,k) in d:
                return d[(pos,k)]
            if pos==last_stone:
                d[(pos,k)] = True
                return True
            else:
                if (k!=0 and pos + k in stones and solve(pos+k,k)):
                    d[(pos,k)] = True
                elif (k-1!=0 and pos + k -1 in stones and solve(pos+k-1,k-1)):
                    d[(pos,k)] = True
                elif (pos+k+1 in stones and solve(pos+k+1,k+1)):
                    d[(pos,k)] = True
                else:
                    d[(pos,k)] = False
                return d[(pos,k)]
        return solve(0,0)