class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        for i in s:
            if i not in sd.keys():
                sd[i]=1
            else:
                sd[i]+=1
        td = {}
        for i in t:
            if i not in td.keys():
                td[i]=1
            else:
                td[i]+=1
        if sd==td:
            return True
        return False