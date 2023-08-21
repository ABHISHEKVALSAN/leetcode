class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        n = len(s)
        i = 0
        j = n-1
        while i<j:
            if s[:i+1]==s[j:] and s.replace(s[:i+1],'')=='':
                return True
            i+=1
            j-=1
        return False
        
