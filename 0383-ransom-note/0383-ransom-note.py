class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        i = 0
        j = 0
        magazine = sorted(list(magazine))
        ransomNote = sorted(list(ransomNote))
        n1 = len(magazine)
        n2 = len(ransomNote)
        print(magazine)
        while i < n1:
            if j==n2:
                return True
            if magazine[i]==ransomNote[j]:
                i+=1
                j+=1
            else:
                i+=1
        if j==n2:
            return True
        return False