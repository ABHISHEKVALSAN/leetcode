class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i]==-1:
                group[i] = i + m
        g0 = {}
        g1 = {}

        dg0 = [0 for _ in range(n+m)]
        dg1 = [0 for _ in range(n)]
        for i, e in enumerate(beforeItems):
            for element in e:
                if group[element]!=group[i]:
                    g0.setdefault(group[element],[]).append(group[i])
                    dg0[group[i]]+=1
                g1.setdefault(element,[]).append(i)
                dg1[i]+=1
        def func(g, dg):
            ans = []
            stack = [k for k in range(len(dg)) if dg[k]==0]
            while stack:
                n = stack.pop()
                ans.append(n)
                for num in g.get(n,[]):
                    dg[num]-=1
                    if dg[num]==0:
                        stack.append(num)
            return ans
        
        tp0 = func(g0,dg0)
        if len(tp0)!=len(dg0): 
            return []

        tp1 = func(g1,dg1)
        if len(tp1)!=len(dg1):
            return []

        m0 = {e:i for i,e in enumerate(tp0)}
        m1 = {e:i for i,e in enumerate(tp1)}

        return sorted([i for i in range(n)], key=lambda x: (m0[group[x]], m1[x]))
