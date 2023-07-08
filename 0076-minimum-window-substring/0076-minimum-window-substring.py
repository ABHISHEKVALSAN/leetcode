class Solution:

    def minWindow(self, s: str, t: str) -> str:
        def is_same_dict(d1, d2):
            for k, v in d2.items():
                if d1[k] < d2[k]:
                    return False
            return True
        n1 = len(s)
        n2 = len(t)
        dt = {}
        for i in t:
            if i in dt:
                dt[i]+=1
            else:
                dt[i]=1
        n = len(s)
        min_len = n
        ans = s
        i_start = 0
        i_end = 0
        ds = {k: 0 for k in dt.keys()}
        flag = False
        while i_end<=n and i_start < n:
            #print(i_start,i_end,end=' ')
            if not is_same_dict(ds,dt):
                if i_end==n:
                    break
                #print('a',ds,dt)
                rc = s[i_end]
                if rc in dt:
                    ds[rc]+=1
                i_end+=1
            else:
                flag = True
                #print('b',ds)
                if i_end-i_start < min_len:
                    min_len = i_end-i_start
                    ans = s[i_start:i_end]
                    #print('*1',ans)
                lc = s[i_start]
                if lc in dt:
                    ds[lc]-=1
                i_start+=1
        if flag:
            return ans
        return ""


            

            