class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool: 
        s = s.split()
        n = len(s)
        if n!=len(pattern):
            return False
        pd = {}
        i=0
        while i<n:
            ch = pattern[i]
            word = s[i]
            if ch in pd:
                if pd[ch]!=word:
                    return False
            else:
                if word in pd.values():
                    return False
                pd[ch]=word
            i+=1
        return True
