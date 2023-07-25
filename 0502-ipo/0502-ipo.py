from bisect import bisect_right
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cp = []
        i = 0
        while i<len(profits):
            pr = profits[i]/capital[i] if capital[i]!=0 else float('inf')
            cp.append([profits[i],pr,capital[i]])
            i+=1
        
        cp.sort()
        while k>0:
            ind = len(cp)-1
            while ind>=0:
                p,pr,c = cp[ind]
                if c<=w:
                    break
                ind-=1
            if ind==-1:
                break
            w+=p
            cp.pop(ind)
            k-=1
        return w

