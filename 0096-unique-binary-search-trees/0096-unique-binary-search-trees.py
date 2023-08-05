class Solution:
    def numTrees(self, n: int) -> int:
        fact = [0,1,2]
        for i in range(3,2*n+1):
            fact.append(fact[-1]*i)
        return int(fact[2*n] / (fact[n+1] * fact[n]))