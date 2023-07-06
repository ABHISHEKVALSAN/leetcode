class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i1 = 0
        i2 = 0
        n1 = len(t)
        n2 = len(s)

        while i1 < n1 and i2 < n2:
            if t[i1]==s[i2]:
                i1+=1
                i2+=1
            else:
                i1+=1
        return i2==n2